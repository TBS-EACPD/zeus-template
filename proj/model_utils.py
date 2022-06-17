from django.conf import settings
from django.db import models
from django.utils import timezone

from zeus.versioning.core import VersionModel


class CustomVersionModel(VersionModel):
    class Meta:
        abstract = True
        ordering = ["business_date"]
        get_latest_by = "business_date"

    system_date = models.DateTimeField(default=timezone.now)
    business_date = models.DateTimeField(default=timezone.now)

    @property
    def previous_version(self):
        return (
            self.__class__.objects.filter(
                eternal_id=self.eternal_id, business_date__lt=self.business_date
            )
            .order_by("business_date")
            .last()
        )


class CustomVersionModelWithEditor(CustomVersionModel):
    class Meta(CustomVersionModel.Meta):
        abstract = True

    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
