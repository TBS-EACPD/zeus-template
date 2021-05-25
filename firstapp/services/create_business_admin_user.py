# services are functions that have side-effects

from django.contrib.auth.models import Group

from proj.models import User
from proj.utils import generate_password

from firstapp.constants import BUSINESS_ADMIN_GROUP_NAME


def create_business_admin_user(username, password=None):
    if password is None:
        password = generate_password()
