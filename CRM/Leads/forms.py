from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

user = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('username',)
        field_classes = {'username' : UsernameField}