from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.shortcuts import redirect

class OrganizerAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.organizer:
            return redirect("leads_list")
        return super().dispatch(request, *args, **kwargs)