from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout



templater = get_renderer('events')

@view_function
def process_request(request):

    params = {}

    # get event
    event = hmod.Event.objects.get(id = request.urlparams[0])

    # get list of products for sale
    products = hmod.Product.objects.all()

    # get list of areas
    areas = hmod.Area.objects.all()

    params['event'] = event
    params['products'] = products
    params['areas'] = areas

    return templater.render_to_response(request, 'event_detail.html', params)
