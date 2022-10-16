from django import forms
from .models import *

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        