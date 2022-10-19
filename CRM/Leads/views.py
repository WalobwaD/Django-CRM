# from audioop import reverse
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

# Create your views here.

def home_view(request):
    return render(request, "Leads/home.html")

@login_required
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads' : leads
    }
    return render(request, 'Leads/leads_list.html', context)

@login_required
def lead_detail(request, pk):
    leads = Lead.objects.get(id = pk)
    context = {
        "lead" : leads
    }
    return render(request, 'Leads/lead_details.html', context )

@login_required
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


@login_required
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("Leads:leads_list")

@login_required
def create_lead(request):
    forms = LeadForm()
    
    if request.method == "POST":
        forms = LeadForm(request.POST)
        
        if forms.is_valid():
            forms.save()
            
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = "dantezwalobwa@gmail.com"

            subject = "Lead Profile Created successfully !"
            message = f"{first_name} {last_name}'s Profile has been created with success, You can confirm if this is done on the leads page.. Thank You!"     
            from_mail = settings.EMAIL_HOST_USER
            to = [email]
            
            send_mail(
                subject,
                message,
                from_mail,
                to,
                fail_silently=False,
            )
            
            
            
            return redirect("Leads:leads_list")
            
    else:
        forms = LeadForm()
    context = {
        "form" : forms
    }
    return render(request, 'Leads/create_lead.html', context)

class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    
    def get_success_url(self):
        return reverse("Leads:login")
    
    class PasswordResetView(PasswordResetView):
        template_name = "registration/password_reset_form.htmls"