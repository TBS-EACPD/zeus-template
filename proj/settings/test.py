from .dev import *

# These settings will speed up testing
DEBUG = False
TEST_RUNNER = "tests.pytest_test_runner.PytestTestRunner"

# this makes tests start quicker
# see https://simpleisbetterthancomplex.com/tips/2016/08/19/django-tip-12-disabling-migrations-to-speed-up-unit-tests.html
def get_app_name(installed_app_path):
    # remap python paths like "django.contrib.auth" and "structure.apps.AppConfig" to their real app-names
    return (
        installed_app_path.replace(".apps.AppConfig", "")
        .replace(".apps.AutodiscoverRulesConfig", "")
        .split(".")[-1]
    )


MIGRATION_MODULES = {get_app_name(app): None for app in INSTALLED_APPS}
