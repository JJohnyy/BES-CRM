from django.core.mail import send_mail
from django.views import generic
from django.contrib import messages
from django.shortcuts import reverse
from .forms import AgentModelForm
from .mixins import OrganiserAndLoginRequiredMixin
from agents.models import Agent, User

# Create your views here.

class AgentListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    """
    agent list, filters based on organisation (oraganisation = organiser)
    """
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        organisation = self.request.user
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    """
    creates a new agent, sets a new password
    """
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password("BohemianEstates123")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user
        )

        send_mail(
            subject='Agent created',
            message="You were added as an agent on BES CRM",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        messages.success(
            self.request, "You have successfully created an agent"
            )
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    """
    agent detail, filters based on organisation
    """    
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user
        return User.objects.filter(organisation=organisation)

class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organisation = self.request.user
        return Agent.objects.filter(organisation=organisation)
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully updated an agent")
        return super(AgentUpdateView, self).form_valid(form)

class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    """
    deletes an agent, redirects back to an agent list if succesfull
    """
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse('agents:agent-list')

