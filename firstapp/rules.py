# These are simple rule functions that return True/False
# Recommended to keep all the signatures void=> Boolean, user=>Boolean or user,obj=>Boolean
# For more complicated authorization logic and rule-composition, "upgrade" to django-rules https://github.com/dfunckt/django-rules

from firstapp.models import DepartmentProfile


def is_user_business_admin(user):
    return "business_admins" in user.group_names


def is_a_dept_user(user):
    return "department_users" in user.group_names


def is_user_specific_dept(user, dept_id):
    if not "department_users" in user.group_names:
        return False

    profile = DepartmentProfile.objects.get(user=user)
    return profile.department_id == dept_id


def can_access_dept(user, dept_id):
    if is_user_business_admin(user):
        return True

    return is_user_specific_dept(user, dept_id)


def can_edit_report(user, report):
    if is_user_business_admin(user):
        return True

    return is_user_specific_dept(user, report.department_id)
