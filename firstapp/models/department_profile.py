from django.db import models

# These models link users and departments together.
# You should only use one of the following models. The 2nd is more flexible.
# You can also use these models to store dept/user-level metadata
#   Don't add fields to django's core User/Group models
#   Don't add fields to the department model


# if users are 1-1 with deparments, this 1-1 profile works nicely
# to check if a user is a department, just check user.dept_profile


class DepartmentProfile(models.Model):
    department = models.OneToOneField(
        "firstapp.Department", on_delete=models.CASCADE, related_name="profile"
    )
    user = models.OneToOneField(
        "proj.User", null=False, related_name="dept_profile", on_delete=models.CASCADE
    )
    extra_field = models.TextField()


# The above won't allow multiple users per department. The below does.
# You also need to create one group per department
# To check if a group is a department, just check group.dept_profile
# To check a user, check all their groups


class DepartmentGroupProfile(models.Model):
    department = models.OneToOneField(
        "firstapp.Department", on_delete=models.CASCADE, related_name="group_profile"
    )
    group = models.OneToOneField(
        "auth.Group", null=False, related_name="dept_profile", on_delete=models.CASCADE
    )
    extra_field = models.TextField()

