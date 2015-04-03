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
        Return list of items, sorted by name
    '''

    params = {}


    # get list of events, sorted by start date
    items = hmod.Item.objects.all().order_by('name')


    # pass list to template
    params['items'] = items


    return templater.render_to_response(request, 'items.html', params)


@view_function
def create(request):

    params = {}

    # create event object
    item = hmod.Item()

    # save new event
    item.save()

    # send user to edit page
    return HttpResponseRedirect('/manager/items.edit/{}/'.format(item.id))

@view_function
def edit(request):

    params = {}

    # try to get event
    try:
        item = hmod.Item.objects.get(id = request.urlparams[0])
    except hmod.Item.DoesNotExist:
        # redirect to event list page
        return HttpResponseRedirect('/manager/items/')

    # initialize event edit form
    form = ItemEditForm(initial={
        'name' : item.name,
        'description': item.description,
        'value': item.value,
        'rental_price': item.rental_price,

    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = ItemEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            print('Form is valid')

            # item event object
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.rental_price = form.cleaned_data['rental_price']


            item.save()

            # send to event list page
            return HttpResponseRedirect('/manager/items/')


    params['form'] = form

    return templater.render_to_response(request, 'items.edit.html', params)

@view_function
def delete(request):

    params = {}

    # try and get event
    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])

    # if event does not exist
    except hmod.Item.DoesNotExist:

        # go back to event list page
        return HttpResponseRedirect('/manager/items/')


    # else, delete event
    item.delete()

    # return to event list page
    return HttpResponseRedirect('/manager/items/')


class ItemEditForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lightsaber'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Used by Darth Vader'}))
    value = forms.DecimalField(max_digits=7,decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '999.99'}))
    rental_price = forms.DecimalField(max_digits=7,decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9.99'}))
