from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home_view(request):
    return render(request, "Leads/home.html")

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads' : leads
    }
    return render(request, 'Leads/leads_list.html', context)

def lead_detail(request, pk):
    leads = Lead.objects.get(id = pk)
    context = {
        "lead" : leads
    }
    return render(request, 'Leads/lead_details.html', context )

def lead_update(request, pk):
    leads = Lead.objects.get(id = pk)
    form = LeadForm(instance=leads)
    
    if request.method == "POST":
        form = LeadForm(request.POST, instance=leads)
        if form.is_valid():
            form.save()
            return redirect("Leads:leads_list")
    
    context = {
        "form" : form,
        "lead" : leads,
    }
    return render(request, 'Leads/lead_update.html', context )

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("Leads:leads_list")

def create_lead(request):
    forms = LeadForm()
    
    if request.method == "POST":
        forms = LeadForm(request.POST)
        
        if forms.is_valid():
            forms.save()
            
            return redirect("Leads:leads_list")
            
    else:
        forms = LeadForm()
    context = {
        "form" : forms
    }
    return render(request, 'Leads/create_lead.html', context)