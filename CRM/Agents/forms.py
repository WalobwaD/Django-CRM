from django import forms
from Leads.models import *

class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        ) 