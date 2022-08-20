from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganiserAndLoginRequiredMixin
from .models import Lead
from agents.forms import AssignAgentForm
from agents.forms import CustomerCreationForm
from leads.forms import (
    LeadModelForm,
    LeadCategoryUpdateForm,
    CategoryModelForm,
)

# Create your views here.



class SignupView(generic.CreateView):
    """
    creates an account and redirects to login page if succesfull
    """
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        messages.success(
            self.request, "You have successfully created an account"
            )
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    """
    lead list view, filter based on organiser or agent
    """
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, agent__isnull=False
                )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation, agent__isnull=False
                )
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, agent__isnull=True
                )
            context.update({
                'unassigned_leads': queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """
    lead detail view, checks if use is an organiser or agent and filter
    """
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile
                )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation
                )
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    """
    cerates a lead, if succesfull, redirects to the lead list
    """
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A lead has been created",
            message="The lead has been created",
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        messages.success(self.request, "Lead was created")
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    """
    updates a lead, if successfull redirects to a lead list
    """
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully updated a lead")
        return super(LeadUpdateView, self).form_valid(form)


class LeadDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    """
    deletes a lead, if succesfull redirects to a lead list
    """
    template_name = 'leads/lead_delete.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    updates a category on a lead
    """
    template_name = "leads/lead_category_update.html"
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse(
            "leads:lead-detail", kwargs={"pk": self.get_object().id}
            )


class CategoryCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    """
    creates a new categoryand adds it to the category list
    """
    template_name = "leads/category_create.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        category = form.save(commit=False)
        category.organisation = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)


class AssignAgentView(OrganiserAndLoginRequiredMixin, generic.FormView):
    """
    assigns an agent to a lead
    """
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)
