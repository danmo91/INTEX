from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod
import hashlib, datetime, random, string
from django.core.mail import send_mail, EmailMessage
# ldap plugins
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO, SEARCH_SCOPE_WHOLE_SUBTREE


templater = get_renderer('homepage')

@view_function
def process_request(request):

    params = {}

    return templater.render_to_response(request, 'index.html', params)



@view_function
def loginform(request):

    params = {}

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            # check ldap


            # login to chf

            #Authenicate and Login
            print('>>>>>>>>>>>>>>>>>>>> Authenticating')
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            print('user:', user)
            if user is not None:
                login(request, user)
                print("logged in")

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            '''
            )


    params['form'] = form

    return templater.render_to_response(request, 'index.loginform.html', params)


@view_function
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('/homepage/index/')

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@view_function
def forgot_password(request):
    params = {}

    form = ForgotPasswordForm()

    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():

            # get user
            user = hmod.User.objects.get(username=form.cleaned_data['username'], email=form.cleaned_data['email'])

            # create temp password
            temp_password = random_generator()
            user.temp_password = temp_password

            # create activation key
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + user.email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            user.activation_key = activation_key

            # expiration date
            user.expiration_date = datetime.date.today() + datetime.timedelta(days=1)
            user.save()

            # email password link embedded with key,
            subject = "CHF- Password Recovery"
            to = [user.email]
            from_email = 'do-not-reply@cheritagefoundation.com'

            params = {
                'activation_link': 'http://127.0.0.1:8000/homepage/index.recover_password/' + activation_key,
                'temp_password': temp_password
            }

            message = templater.render(request, 'recover_password_email.html', params)

            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            '''
            )

            # user clicks link and it reset's password to temp password IF within 24 hours



    params['form'] = form
    return templater.render_to_response(request, 'index.forgot_password.html', params)

@view_function
def recover_password(request):

    params = {}

    # user clicked link

    # get activation key
    activation_key = request.urlparams[0]

    # lookup user
    user = hmod.User.objects.get(activation_key=activation_key)
    print('user:', user)

    # check if expiration date has passed
    expiration_date = user.expiration_date

    if expiration_date > datetime.date.today():
        # change password and login user
        saved_username = user.username
        temp_password = user.temp_password
        user.set_password(user.temp_password)
        user.save()
        user = authenticate(username = saved_username, password = temp_password)
        login(request, user)




    return templater.render_to_response(request, 'index.html', params)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):

        if self.is_valid():

            print('checking ldap')
            # check ldap

            # create server, make connection change server to cheritagefoundation.com later
            s = Server('www.cheritagefoundation.com', port=12345, get_info=GET_ALL_INFO)

            c = Connection(
                  s,
                  auto_bind = True,
                  user = self.cleaned_data['username'] + '@cheritagefoundation.local',
                  password= self.cleaned_data['password'],
                  authentication=AUTH_SIMPLE,
                  client_strategy=STRATEGY_SYNC
                )

            search_results = c.search(
              search_base = 'CN=Users,DC=cheritagefoundation,DC=local',
              search_filter = '(samAccountName=' + self.cleaned_data['username'] + ')',
              search_scope = SEARCH_SCOPE_WHOLE_SUBTREE,
              attributes = [
                'givenName',
                'sn',
                'l',
                'streetAddress',
                'postalCode',
                'st',
                'mobile',
                'info',
              ])

            # if ldap, then login to ldap
            if search_results:

                # get info from active directory
                user_info = c.response[0]['attributes']

                user = hmod.User.objects.get_or_create(
                    username=self.cleaned_data['username'],
                    first_name = user_info['givenName'],
                    last_name = user_info['sn'],
                    phone = user_info['mobile'],
                    email = user_info['info'],
                    )
                print('user:', user)

                user = hmod.User.objects.get(username = self.cleaned_data['username'])
                print('user:', user)


                # set password
                user.set_password(self.cleaned_data['password'])
                user.save()

                print('user_info:', user_info)
                print('first_name:', user_info['givenName'])
                print('last_name:', user_info['sn'])
                print('city:', user_info['l'])
                print('street:', user_info['streetAddress'])
                print('zip_code:', user_info['postalCode'])
                print('state:', user_info['st'])
                print('phone:', user_info['mobile'])
                print('email:', user_info['info'])

            else:

                user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
                if user is None:
                    raise forms.ValidationError("Incorrect username and password")

        return self.cleaned_data

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dan@gmail.com'}))

    def clean(self):
        if self.is_valid():
            try:
                user = hmod.User.objects.get(username=self.cleaned_data['username'], email=self.cleaned_data['email'])
            except hmod.User.DoesNotExist:
                # redirect to event list page
                raise forms.ValidationError("Username and email did not match")

        return self.cleaned_data
