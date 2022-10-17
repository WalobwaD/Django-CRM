from django.urls import reverse
from importlib import import_module
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Leads.models import Agent
from .forms import AgentCreateForm


# Create your views here.
class AgentsList(LoginRequiredMixin, ListView):
    template_name = "Agents/agents_list.html"
    context_object_name = "agents" 
    
    def get_queryset(self):
        return Agent.objects.all()
    
# class AgentsDetails(LoginRequiredMixin, DetailView):
#     template_name = "Agents/agents_create"
#     context_object_name = "agent"
    

class AgentsCreate(LoginRequiredMixin, CreateView):
    template_name = "Agents/create_agent.html" 
    form_class= AgentCreateForm
    
    def get_success_url(self):
        return reverse("Agents:agents")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentsCreate, self).form_valid(form)

# class AgentsUpdate(LoginRequiredMixin, UpdateView):
#     template_name = "Agents/agents_list"
#     context_object_name = "agents" 
    
#     def get_queryset(self):
#         return Agent.objects.all()