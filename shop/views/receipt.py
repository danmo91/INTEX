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

    # Show purchased items on receipt page

    if 'shopping_cart' not in request.session:

        request.session['shopping_cart'] = {}

    item_ids = request.session['shopping_cart']


    items = {}

    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)


        items[item.id] = item_container

    params['items'] = items


    # clear out shopping cart
    del request.session['shopping_cart']


    return templater.render_to_response(request, 'receipt.html', params)
