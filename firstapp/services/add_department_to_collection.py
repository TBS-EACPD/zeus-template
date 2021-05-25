# services are functions that have side-effects

from django.contrib.auth.models import Group

from proj.models import User
from proj.utils import generate_password

from firstapp.constants import DEPT_GROUP_NAME
from firstapp.models import DepartmentProfile


def username_for_org(dept):
    return f"{dept.get_base_username()}_mybusiness"


def _create_dept_user(dept, password=None):
    if password is None:
        password = generate_password()

    username = username_for_org(dept)

    u = User.objects.create_user(username=username, password=password)
    g = Group.objects.get(name=DEPT_GROUP_NAME)
    u.groups.add(g)

    return u


def add_department_to_collection(department, password=None):
    user = _create_dept_user(department, password)
    profile = DepartmentProfile.objects.create(user=user, department=department)

    return profile
