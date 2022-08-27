from django import forms
from agents.models import Agent
from leads.models import Lead

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
             'user.email',
             'username',
             'first_name',
             'last_name',
         )
        


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organisation=request.user)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
