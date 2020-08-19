from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, PartnerForm
from .utils import *


def index(request):
    return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


class LoginView(View):
    template_name = 'register/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return request.user.login_redirect()
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            login(request, user)
            return user.login_redirect()
        else:
            messages.error(request, 'Your username or password is incorrect.')
            return redirect('login')


class SignupView(View):
    user_form = UserForm
    partner_form = PartnerForm
    context = { 'user_form': user_form, 'partner_form': partner_form }
    template_name = 'register/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(request.POST)
        partner_form = self.partner_form(request.POST)
        if user_form.is_valid:
            user = user_form.save(commit=False)
        else:
            messages.error(request, user_form.errors)
            return redirect('signup')
        if partner_form.is_valid():
            partner = partner_form.save(commit=False)
            cleaned_data = partner_form.clean()
            first_name, last_name = get_names(cleaned_data.get('contact_name'))
            email = cleaned_data.get('email')
        else:
            messages.error(request, partner_form.errors)
            return redirect('signup')
        save_both(user, partner, first_name, last_name, email)
        return user.login_redirect()
