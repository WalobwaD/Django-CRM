from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView


app_name = 'Leads'

urlpatterns = [
    path('all-leads/', lead_list, name="leads_list"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('create/', create_lead, name='create'),
    path('<int:pk>/update/', lead_update, name="update"),
    path('<int:pk>/delete', lead_delete, name="delete"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
