from django.contrib.staticfiles.management.commands.runserver import Command as RunServer

# note that we use django.contrib.staticfiles instead of django.core.management because the staticfiles app overrides this


class Command(RunServer):
    def check(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("SKIPPING SYSTEM CHECKS!\n"))

    def check_migrations(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("SKIPPING MIGRATION CHECKS!\n"))
