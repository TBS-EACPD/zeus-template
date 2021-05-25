from django.contrib.auth.models import Group
from django.db import transaction

import pytest

from firstapp import constants, services
from firstapp.models import Department
from firstapp.models.factories import DepartmentFactory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    without this, tests (including old-style) have to explicitly declare db as a dependency
    https://pytest-django.readthedocs.io/en/latest/faq.html#how-can-i-give-database-access-to-all-my-tests-without-the-django-db-marker
  """
    pass


@pytest.fixture(scope="package")
def _root_package_scoped_autofixture(django_db_setup, django_db_blocker):
    """
        this is a mouthful, but this essentially applied 
    """

    with django_db_blocker.unblock():
        # Wrap in try + atomic block to do non crashing rollback
        try:
            with transaction.atomic():
                yield
                raise Exception
        except Exception:
            pass


@pytest.fixture(scope="package", autouse=True)
def create_groups(_root_package_scoped_autofixture):
    Group.objects.create(name=constants.BUSINESS_ADMIN_GROUP_NAME)
    Group.objects.create(name=constants.DEPT_GROUP_NAME)


@pytest.fixture(scope="package", autouse=True)
def create_mits_dept(_root_package_scoped_autofixture):
    mits = DepartmentFactory(tbs_dept_code="MITS")
    services.add_department_to_collection(mits, password="123")


@pytest.fixture
def mits():
    return Department.objects.get(tbs_dept_code="MITS")


@pytest.fixture
def mits_user(mits):
    return mits.profile.user


@pytest.fixture
def mits_client(client, mits_user):
    client.force_login(mits_user)
    return client
