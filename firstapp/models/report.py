from django.db import models

from proj.model_utils import CustomVersionModelWithEditor


class Report(models.Model):
    title = models.TextField()
    body = models.TextField()
    department = models.ForeignKey(
        "firstapp.Department", null=False, on_delete=models.CASCADE
    )


class ReportVersions(CustomVersionModelWithEditor):
    live_model = Report
