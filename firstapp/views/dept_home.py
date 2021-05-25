from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from firstapp.models import Department
from firstapp.rules import can_access_dept


class DeptHome(TemplateView, LoginRequiredMixin):
    template_name = "firstapp/dept-home.html"

    def dispatch(self, *args, **kwargs):
        if not can_access_dept(self.request.user, self.kwargs["dept_id"]):
            raise PermissionDenied("forbidden")

        return super().dispatch(*args, **kwargs)

    def get_context_data():
        dept = Department.objects.get(id=self.kwargs["dept_id"])
        return {"department": dept}

