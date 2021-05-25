from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms.models import ModelForm
from django.views.generic import UpdateView

from proj.text import tm

from firstapp.models import Report
from firstapp.rules import can_edit_report


class UpdateReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["title", "body"]


class UpdateReport(UpdateView):
    template_name = "firstapp/update-report.html"
    form_class = UpdateReportForm
    queryset = Report.objects.all()

    def dispatch(self, *args, **kwargs):
        report = Report.objects.get(id=self.kwargs["pk"])
        if not can_edit_report(self.request.user, report):
            raise PermissionDenied("forbidden")

        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.request.build_absolute_uri()

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, tm("saved_successfully"))
        return super().form_valid(form)
