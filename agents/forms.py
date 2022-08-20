from django import forms
<<<<<<< HEAD
from agents.models import Agent, User
from leads.models import Lead
=======
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
>>>>>>> parent of 2fa6725 (mademigration)




class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = (
         #    'email',
         #    'username',
         #    'first_name',
         #    'last_name',
         #)
        fields = '__all__'


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
