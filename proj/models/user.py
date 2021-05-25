# It's recommended to always create a custom User model

from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Prefetch
from django.utils.functional import cached_property


class GroupPrefetcherManager(UserManager):
    use_for_related_fields = True

    def get_queryset(self):
        return (
            super(GroupPrefetcherManager, self)
            .get_queryset()
            .select_related("dept_profile")
            .prefetch_related(Prefetch("groups", to_attr="group_list"))
            .prefetch_related(Prefetch("group_list__dept_profile"))
        )


class User(AbstractUser):
    objects = GroupPrefetcherManager()
    plain_objects = UserManager()

    class Meta:
        base_manager_name = "objects"

    @cached_property
    def group_names(self):
        # this makes it easier to check for groups without N+1 worries

        if not hasattr(self, "group_list"):
            self.group_list = list(self.groups.all())

        return [g.name for g in self.group_list]

    def is_department_user(self):
        # if using 1-1 dept profiles
        if self.dept_profile:
            return True
        # if using group dept profiles
        for g in self.group_list:
            if g.department_profile:
                return True

        return False

    def is_specific_department(self, org_id):
        # if using 1-1 dept profiles
        if self.dept_profile:
            return self.dept_profile.id == org_id

        # if using group dept profiles
        for g in self.group_list:
            if g.department_profile:
                return g.department_profile.department_id == org_id

        return False

    @property
    def department(self):
        if self.dept_profile:
            return self.dept_profile.department

        # if using group dept profiles
        for g in self.group_list:
            if g.department_profile:
                return g.department_profile.department
