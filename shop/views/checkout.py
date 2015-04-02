from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from localflavor.us.us_states import STATE_CHOICES




templater = get_renderer('shop')

@view_function
def process_request(request):

    params = {}

    # check to see if user needs to login to checkout

    user = request.user
    if request.user.username == '':

        request.session['login_required'] = True
        return HttpResponseRedirect('/shop/index/')



    # Show items in cart on checkout page

    if 'shopping_cart' not in request.session:

        request.session['shopping_cart'] = {}

    item_ids = request.session['shopping_cart']


    items = {}

    for key,value in item_ids.items():

        item = hmod.Product.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)


        items[item.id] = item_container

    params['items'] = items

    # get items in cart
    num_items = 0

    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items


    return templater.render_to_response(request, 'confirm_order.html', params)

@view_function
def enter_payment(request):

    params = {}

    form = CheckoutForm()


    






    params['form'] = form

    # get items in cart
    num_items = 0

    if 'shopping_cart' in request.session:
        num_items = len(request.session['shopping_cart'])

    params['num_items'] = num_items


    return templater.render_to_response(request, 'enter_payment.html', params)


class CheckoutForm(forms.Form):
    address = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'street'}))
    city = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))


    # state = forms.CharField(required=True, widget=forms.Select(choices=STATE_CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'multiple title':'state'} ))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}))


    zip_code = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip'}))
    creditcard = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'credit card number'}))
    expiration = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'expiration mm/yy'}))
    csv = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ccv'}))
