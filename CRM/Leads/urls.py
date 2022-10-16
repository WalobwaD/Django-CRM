from django.urls import path
from .views import *


app_name = 'Leads'

urlpatterns = [
    path('', home_view, name="home"),
    path('all-leads/', lead_list, name="leads_list"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('create/', create_lead, name='create'),
    path('<int:pk>/update/', lead_update, name="update"),
    path('<int:pk>/delete', lead_delete, name="delete")
]
