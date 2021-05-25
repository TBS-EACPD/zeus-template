from django.contrib.auth.models import Group
from django.db import transaction

from firstapp.models import Department, Report
from firstapp.services import add_department_to_collection, create_business_admin_user

from .create_initial_groups import run as create_initial_groups


@transaction.atomic()
def run():
    create_initial_groups()

    admin = create_business_admin_user("admin1", password="abc")

    # NEVER create departments in production, always get them from TBS
    d1 = Department.objects.create(
        id=1,
        legal_name_en="department of mittens",
        legal_name_fr="ministère des mittaines",
        abbr_en="MITS",
        abbr_fr="MITS",
    )
    d2 = Department.objects.create(
        id=2,
        legal_name_en="department of kittens",
        legal_name_fr="ministère des kittaines",
        abbr_en="KITS",
        abbr_fr="KITS",
    )

    add_department_to_collection(d1, password="abc")
    add_department_to_collection(d2, password="abc")

    r1 = Report.objects.create(
        title="report1", body="a great first mittens report", department=d1
    )
    r2 = Report.objects.create(
        title="report2", body="a great second mittens report", department=d1
    )
    r3 = Report.objects.create(
        title="report2", body="a great kittens report", department=d2
    )
