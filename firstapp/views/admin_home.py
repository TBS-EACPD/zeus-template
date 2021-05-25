from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from firstapp.models import Department
from firstapp.rules import is_user_business_admin


class AdminHome(TemplateView, LoginRequiredMixin):
    template_name = "firstapp/admin-home.html"

    def dispatch(self, *args, **kwargs):
        if not is_user_business_admin(self.request.user):
            raise PermissionDenied("forbidden")

        return super().dispatch(*args, **kwargs)

    def get_context_data():
        depts = Department.objects.all()
        return {"departments": depts}
