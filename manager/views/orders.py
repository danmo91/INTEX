from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetimewidget.widgets import DateWidget
import datetime
from django import forms
import homepage.models as hmod


templater = get_renderer('manager')

@view_function
def process_request(request):
    '''
        Return list of orders, sorted by date
    '''

    params = {}

    form = OrderEditForm()


    # get list of events, sorted by start date
    orders = hmod.Order.objects.all().order_by('order_date')


    # pass list to template
    params['orders'] = orders


    return templater.render_to_response(request, 'orders.html', params)


@view_function
def create(request):

    params = {}

    # create event object
    order = hmod.Order()

    order.user = hmod.User()
    # order.user.first_name = 'None'
    # order.user.last_name = ''

    # save new event
    order.save()

    print('new order:', order)

    # send user to edit page
    return HttpResponseRedirect('/manager/orders.edit/{}'.format(order.id))

@view_function
def edit(request):

    params = {}

    # try to get event
    try:
        order = hmod.Order.objects.get(id = request.urlparams[0])
    except hmod.Order.DoesNotExist:
        # redirect to event list page
        return HttpResponseRedirect('/manager/orders/')


    if order.user is not None:
    # initialize event edit form
        form = OrderEditForm(initial={
            'order_date' : order.order_date,
            'total': order.total,
            'user': order.user.first_name + ' ' + order.user.last_name,
        })
    else:
        form = OrderEditForm()

    # if POST
    if request.method == 'POST':
        # get form from request
        form = OrderEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            # item event object
            order.order_date = form.cleaned_data['order_date']
            order.total = form.cleaned_data['total']

            split_user =  form.cleaned_data['user'].split(" ")

            user_first_name = split_user[0]
            user_last_name = split_user[1]

            user = hmod.User.objects.get(first_name = user_first_name, last_name = user_last_name)

            print('User:', user)

            order.user = user

            order.save()

            # send to event list page
            return HttpResponseRedirect('/manager/orders/')


    params['form'] = form

    return templater.render_to_response(request, 'orders.edit.html', params)

@view_function
def delete(request):

    params = {}

    # try and get event
    try:
        order = hmod.Order.objects.get(id=request.urlparams[0])

    # if event does not exist
    except hmod.Order.DoesNotExist:

        # go back to event list page
        return HttpResponseRedirect('/manager/orders/')


    # else, delete event
    order.delete()

    # return to event list page
    return HttpResponseRedirect('/manager/orders/')

def get_choices():

    # get list of users
    CHOICES = []

    c = ('','')

    CHOICES.append(c)

    all_users = hmod.User.objects.all()

    # get first and last name

    for user in all_users:

        choice = (user.first_name + ' ' + user.last_name, user.first_name + ' ' + user.last_name)

        CHOICES.append(choice)

    return CHOICES


class OrderEditForm(forms.Form):
    order_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-04-05'}))
    total = forms.DecimalField(max_digits=7,decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '30.25'}))

    CHOICES = list(get_choices())
    print('choices:', CHOICES)

    user = forms.CharField(required=True, widget=forms.Select(choices=CHOICES, attrs={'class': 'form-control selectpicker', 'data-width':'100%', 'title':'User'} ))
