from django.urls import path
from .views import *

app_name = "Agents"

urlpatterns = [
    path('all_agents/', AgentsList.as_view(), name="agents"),
    # path('<int:pk>/', AgentsDetails.as_view(), name="agent_details"),
    path('create/', AgentsCreate.as_view(), name="create"),
    # path('<int:pk>/update/', AgentsUpdate.as_view(), name="update"),
]
