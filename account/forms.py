from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    college = forms.CharField(max_length=254, required=True)
    project = forms.CharField(widget=forms.Textarea)
    country = CountryField().formfield(blank_label='Select Country')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email', 'password1', 'password2' ,'college','country','project',)

