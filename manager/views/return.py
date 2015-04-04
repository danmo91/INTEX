from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetimewidget.widgets import DateWidget
from django.core.mail import send_mail, EmailMessage
import datetime
from django import forms
import homepage.models as hmod
from decimal import Decimal


templater = get_renderer('manager')

@view_function
def process_request(request):

    params = {}

    rentals = hmod.Rental.objects.filter(returned = False)

    params['rentals'] = rentals

    return templater.render_to_response(request, 'return.html', params)


@view_function
def return_form(request):

    params = {}

    # get rental information
    object_id = request.urlparams[0]
    rental = hmod.Rental.objects.get(id=object_id)

    # get late fee
    late_fee = 0.00
    if rental.due_date < datetime.date.today():
        late_fee = 3.99

    form = ReturnForm()

    if request.method == 'POST':

        form = ReturnForm(request.POST)
        if form.is_valid():
            rental.damages = form.cleaned_data['damage']
            rental.return_date = datetime.date.today()
            rental.returned = True
            rental.save()

            if rental.item:
                item = rental.item
                item.available = True
                item.save()

            # user = rental.user
            # if not form.cleaned_data['late_fee_waived']:
            #     Decimal.add(user.account_balance, late_fee)
            #     print('pay late fee')
            #
            # if not form.cleaned_data['damage_fee_waived']:
            #     Decimal.add(user.account_balance, Decimal(form.cleaned_data['damage_fee']))
            #     print('pay damage fee')

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            '''
            )

    params['late_fee'] = late_fee
    params['form'] = form
    params['rental'] = rental

    return templater.render_to_response(request, 'return_form.html', params)

@view_function
def send_email(request):
    params = {}

    # get list of overdue rentals
    start = datetime.date.today() - datetime.timedelta(days=365)
    end = datetime.date.today() - datetime.timedelta(days=1)
    overdue_rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False)
    print('over_due:', overdue_rentals)


    # get users emails
    user_emails = []
    for rental in overdue_rentals:
        if rental.user:
            if rental.user.email != '':
                if rental.user.email not in user_emails:
                    user_emails.append(rental.user.email)

    print('user_emails:', user_emails)

    # send email to each user
    if user_emails:
        for email in user_emails:

            # get list of over_due rentals
            user = hmod.User.objects.get(email=email)
            rentals = hmod.Rental.objects.filter(due_date__range = (start, end), returned=False, user = user)
            params['rentals'] = rentals
            params['date'] = datetime.date.today()
            params['user'] = user.full_name


            #Send Email
            if  email != '':
                subject = "Your Rental is Overdue"
                to = [email]
                from_email = 'dan.morain91@gmail.com'

                message = templater.render(request, 'overdue_email.html', params)

                msg = EmailMessage(subject, message, to=to, from_email=from_email)
                msg.content_subtype = 'html'
                msg.send()

        return HttpResponse('1')


    return HttpResponse('0')


class ReturnForm(forms.Form):

    YES_NO = ((True, 'Yes'), (False, 'No'))

    damage = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Damage Details Ex. No Water Left'}))
    # late_fee = forms.CharField(required=True, widget=forms.Select(choices=CHOICES, attrs={'class': 'selectpicker', 'data-width':'100%', 'title':'Late Fee'} ))
    damage_fee = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Damage Fee: $2.00',}))
    late_fee_waived = forms.BooleanField(label='Waive Late Fee', required=False)
    damage_fee_waived = forms.BooleanField(label='Waive Damage Fee',required=False)
