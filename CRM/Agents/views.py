from django.urls import reverse
from importlib import import_module
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from Leads.models import Agent
from .forms import AgentCreateForm
from .mixins import OrganizerAndLoginRequiredMixin


# Create your views here.
class AgentsList(OrganizerAndLoginRequiredMixin, ListView):
    template_name = "Agents/agents_list.html"
    context_object_name = "agents" 
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
# class AgentsDetails(LoginRequiredMixin, DetailView):
#     template_name = "Agents/agents_create"
#     context_object_name = "agent"
    

class AgentsCreate(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "Agents/create_agent.html" 
    form_class= AgentCreateForm
    
    def get_success_url(self):
        return reverse("Agents:agents")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentsCreate, self).form_valid(form)

class AgentDetails(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = "Agents/agent_details.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
class AgentDelete(DeleteView):
    template_name = "Agents/agent_delete.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
    def get_success_url(self):
        return reverse("Agents:agents")
    
    
class AgentUpdate(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'Agents/agent_update.html'
    form_class = AgentCreateForm
    
    def get_success_url(self):
        return reverse("Agents:agents")
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    