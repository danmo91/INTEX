from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod
import datetime


templater = get_renderer('manager')

@view_function
def process_request(request):

    params = {}

    # get list of events, sorted by start date
    rentals = hmod.Rental.objects.all().order_by('due_date')


    # pass list to template
    params['rentals'] = rentals

    return templater.render_to_response(request, 'rentals.html', params)

@view_function
def create(request):

    params = {}

    # create event object
    rental = hmod.Rental()

    # save new event
    rental.save()

    # send user to edit page
    return HttpResponseRedirect('/manager/rentals.edit/{}/'.format(rental.id))

@view_function
def edit(request):

    params = {}

    # try to get event
    try:
        rental = hmod.Rental.objects.get(id = request.urlparams[0])
    except hmod.Rental.DoesNotExist:
        # redirect to event list page
        return HttpResponseRedirect('/manager/rentals/')

    # initialize event edit form
    form = RentalEditForm(initial={
        'description': rental.description,
        'rental_date': rental.rental_date,
        'due_date': rental.due_date,

    })

    # if POST
    if request.method == 'POST':
        # get form from request
        form = RentalEditForm(request.POST)

        # if form is valid
        if form.is_valid():

            # item event object
            rental.description = form.cleaned_data['description']
            rental.rental_date = form.cleaned_data['rental_date']
            rental.due_date = form.cleaned_data['due_date']


            rental.save()

            # send to event list page
            return HttpResponseRedirect('/manager/rentals/')


    params['form'] = form

    return templater.render_to_response(request, 'rentals.edit.html', params)

@view_function
def delete(request):

    params = {}

    # try and get event
    try:
        rental = hmod.Rental.objects.get(id=request.urlparams[0])

    # if event does not exist
    except hmod.Rental.DoesNotExist:

        # go back to event list page
        return HttpResponseRedirect('/manager/rentals/')


    # else, delete event
    rental.delete()

    # return to event list page
    return HttpResponseRedirect('/manager/rentals/')


@view_function
def overdue(request):

    params = {}

    today = datetime.date.today()
    start_date = datetime.date(today.year-20,today.month,today.day)
    end_date = datetime.date(today.year,today.month,today.day-1)


    overdue_items = hmod.Rental.objects.filter(due_date__range = (start_date, end_date))

    params['items'] = overdue_items

    return templater.render_to_response(request, 'rentals.overdue.html', params)


class RentalEditForm(forms.Form):
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Not another pony ride'}))
    rental_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-04-05'}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-04-05'}))
