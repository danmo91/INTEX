from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.contrib.auth import authenticate, login, logout


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
            #Authenicate and Login
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            print(user)
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

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):

        if self.is_valid():

            user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
            if user is None:
                raise forms.ValidationError("Incorrect username and password")

        return self.cleaned_data
