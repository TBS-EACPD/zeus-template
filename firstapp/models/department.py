from django.db import models
from django.utils.translation import get_language

from proj.models import User


class ManualDepartmentModificationError(Exception):
    pass


class DepartmentManager(models.Manager):
    def create(self, *args, **kwargs):
        raise ManualDepartmentModificationError(
            "Don't create departments directly! use dangerously_create if you know what you're doing"
        )

    def dangerously_create(self, *args, **kwargs):
        return super().create(*args, **kwargs)


class Department(models.Model):
    """
        this class should ONLY contain fields that come from titan
        extra fields should go in a 1-1 linked model, like department_profile
    """

    objects = DepartmentManager()

    id = models.IntegerField(primary_key=True)
    tbs_dept_code = models.CharField(max_length=10)
    legal_name_en = models.TextField()
    legal_name_fr = models.TextField()
    applied_title_en = models.TextField()
    applied_title_fr = models.TextField()
    abbr_en = models.TextField()
    abbr_fr = models.TextField()

    @property
    def name(self):
        if get_language() == "en":
            return self.applied_title_en or self.legal_name_en
        else:
            return self.applied_title_fr or self.legal_name_fr

    @property
    def abbr(self):
        if get_language() == "en":
            return self.abbr_en
        else:
            return self.abbr_fr

    def get_base_username(self):
        """
            used to create usernames for organizations, e.g. rcmp-grc, pspc-spac, etc. 
        """
        username = None

        first_choice = self.abbr_en
        second_choice = f"{self.abbr_en}-{self.abbr_fr}"
        third_choice = str(self.id)

        if self.abbr_en:
            if (
                self.abbr_en == self.abbr_fr
                and not User.objects.filter(username__icontains=first_choice).exists()
            ):
                username = first_choice

            elif (
                self.abbr_fr
                and not User.objects.filter(username__icontains=second_choice).count()
            ):
                username = f"{self.abbr_en}-{self.abbr_fr}"

        else:
            username = third_choice

        # some abbreviations have spaces in them!
        without_spaces = username.replace(" ", "").lower()

        return without_spaces

