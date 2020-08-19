from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Partner, User


class UserForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ['password1']


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['email', 'company_name', 'contact_name']
