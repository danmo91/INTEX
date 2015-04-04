from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetimewidget.widgets import DateWidget
import datetime
from django import forms
import homepage.models as hmod
from decimal import Decimal


templater = get_renderer('manager')

@view_function
def process_request(request):

    params = {}

    form = ReturnForm()

    if request.method == "POST":

        form = ReturnForm(request.POST)
        if form.is_valid():

            # lookup item
            rental = hmod.Rental.objects.get(description = form.cleaned_data['name'], returned = False)
            print('rental:', rental)
            rental.return_date = datetime.date.today()
            rental.damages = form.cleaned_data['damage']
            rental.returned = True
            rental.save()

            user = rental.user
            user.account_balance += Decimal(form.cleaned_data['late_fee']) + Decimal(form.cleaned_data['damage_fee'])
            print('account balance:', user.account_balance)

            item = rental.item
            item.available = True
            item.save()

            return HttpResponseRedirect('/homepage/')



    params['form'] = form

    return templater.render_to_response(request, 'return.html', params)


class ReturnForm(forms.Form):

    CHOICES = (
        ('',''),
        ('0.00','0.00'),
        ('5.00','5.00'),
        ('10.00','10.00'),
        ('15.00','15.00'),
        ('20.00','20.00'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name: "Knife"'}))
    damage = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Damages: Ruined for life', 'style':'margin-top:15px;'}))
    late_fee = forms.CharField(required=True, widget=forms.Select(choices=CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'title':'Late Fee'} ))
    damage_fee = forms.CharField(required=True, widget=forms.Select(choices=CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'title':'Damage Fee'} ))
    late_fee_waived = forms.BooleanField(label="Waive Late Fee", required=False)
    damage_fee_waived = forms.BooleanField(label="Waive Damage Fee", required=False)
