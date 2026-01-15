from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class StaffRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return HttpResponseForbidden("Staff access only")

        return super().dispatch(request, *args, **kwargs)