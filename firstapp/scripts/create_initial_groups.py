from django.contrib.auth.models import Group
from django.db import transaction

from firstapp.constants import BUSINESS_ADMIN_GROUP_NAME, DEPT_GROUP_NAME


@transaction.atomic()
def run():
    Group.objects.create(name=DEPT_GROUP_NAME)
    Group.objects.create(name=BUSINESS_ADMIN_GROUP_NAME)
