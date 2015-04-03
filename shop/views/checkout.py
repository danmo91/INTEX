from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from localflavor.us.us_states import STATE_CHOICES
import requests
import datetime




templater = get_renderer('shop')

@view_function
def process_request(request):

    params = {}

    # check to see if user needs to login to checkout

    user = request.user
    if request.user.username == '':

        request.session['login_required'] = True
        return HttpResponseRedirect('/shop/index/')



    # get shopping_cart items
    items = {}

    if 'shopping_cart' in request.session:

        item_ids = request.session['shopping_cart']



        for key,value in item_ids.items():

            item = hmod.Product.objects.get(id = key)

            item_container = []
            item_container.append(item)
            item_container.append(value)


            items[item.id] = item_container

    params['items'] = items

    # get rental_cart items
    rentals = []
    if 'rental_cart' in request.session:

        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rental = hmod.Item.objects.get(id=rental_id)
            rentals.append(rental)

    params['rentals'] = rentals

    return templater.render_to_response(request, 'confirm_order.html', params)

@view_function
def enter_payment(request):

    params = {}

    form = CheckoutForm()

    if request.method == 'POST':

        # get form
        form = CheckoutForm(request.POST)

        if form.is_valid():

            # check if user has an address
            user = hmod.User.objects.get(id=request.user.id)
            has_address = hmod.Address.objects.filter(user = user)

            if has_address.count() == 0:

                # save address information
                address = hmod.Address()

                address.street = form.cleaned_data['street']
                address.city = form.cleaned_data['city']
                address.state = form.cleaned_data['state']
                address.zip_code = form.cleaned_data['zip_code']
                address.save()

                # associate user with address
                address.user = user
                address.save()

            return HttpResponseRedirect('/shop/checkout.charge_card')


    params['form'] = form

    return templater.render_to_response(request, 'enter_payment.html', params)

def get_total(request):

    # get list of items in shopping_cart
    product_ids = request.session['shopping_cart']

    total = 0

    for product_id in product_ids:
        product = hmod.Product.objects.get(id=product_id)
        total += product.current_price

    # don't forget rental_cart

    return total

@view_function
def charge_card(request):

    params = {}

    params['form'] = CheckoutForm()


    # should i do this in the clean method?  When do i want to charge??

    # send the request with the data
    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = 'aa846fb6f04d54c4b952561399e40d84'

    print("API_KEY:", API_KEY)

    r = requests.post(API_URL, data={
        'apiKey': 'aa846fb6f04d54c4b952561399e40d84',
        'currency': 'usd',
        'amount': '5.99', # my total
        'type': 'Visa',
        'number': '4732817300654',
        'exp_month': '10',
        'exp_year': '15',
        'cvc': '411',
        'name': 'Cosmo Limesandal',
        'description': 'Charge for cosmo@is411@byu.edu',
    })

    # check repsonse text
    print(r.text)

    # parse response dictionary
    resp = r.json()
    if 'error' in resp:
        print('ERROR: ', resp['error'])

    else:
        print(resp.keys())
        print(resp['ID'])

        # finish the transaction and redirect

        # if order, create order object
        if len(request.session['shopping_cart']) > 0:

            order = hmod.Order()

            order.order_date = datetime.date.today()
            order.total = get_total(request)
            user = hmod.User.objects.get(id = request.user.id)
            order.user = user
            order.charge_id = resp['ID']
            order.save()

        # if rental, create rental objects for each rental
        if len(request.session['rental_cart']) > 0:
            rental_ids = request.session['rental_cart']

            for rental_id in rental_ids:
                r = hmod.Item.objects.get(id=rental_id)

                rental = hmod.Rental()
                rental.description = r.name
                rental.rental_date = datetime.date.today()
                rental.due_date = (datetime.date.today() + datetime.timedelta(days=30))
                rental.available = False
                rental.charge_id = resp['ID']
                user = hmod.User.objects.get(id=request.user.id)
                rental.user = user
                rental.save()

        # redirect to receipt
        return HttpResponseRedirect('/shop/checkout.receipt')



    return templater.render_to_response(request, 'enter_payment.html', params)

@view_function
def receipt(request):

    params = {}

    # get items in shopping_cart
    items = {}

    if 'shopping_cart' in request.session:
        item_ids = request.session['shopping_cart']

        for key,value in item_ids.items():

            item = hmod.Product.objects.get(id = key)

            item_container = []
            item_container.append(item)
            item_container.append(value)


            items[item.id] = item_container

            # clear out shopping cart
            del request.session['shopping_cart']

    # pass to template
    params['items'] = items

    # get items in rental_cart
    rentals = []

    if 'rental_cart' in request.session:
        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rental = hmod.Item.objects.get(id=rental_id)
            rentals.append(rental)

        # delete rental_cart
        del request.session['rental_cart']

    # pass to template
    params['rentals'] = rentals

    # get user's address
    user = hmod.User.objects.get(id=request.user.id)
    print('user:', user)
    address = hmod.Address.objects.get(user=user)
    print('address:', address)

    params['address'] = address

    return templater.render_to_response(request, 'receipt.html', params)


class CheckoutForm(forms.Form):
    street = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'street'}))
    city = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))


    # state = forms.CharField(required=True, widget=forms.Select(choices=STATE_CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'multiple title':'state'} ))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}))


    zip_code = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip'}))
    creditcard = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'credit card number'}))
    expiration = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'expiration mm/yy'}))
    cvc = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cvc'}))
