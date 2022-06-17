from decouple import config

from .base import *

# Frequently toggled:
ENABLE_TOOLBAR = True
PRINT_ALL_DB_QUERIES = False
DEBUG = True
TEMPLATE_DEBUG = True
DEBUG_FORM_FIELDS = True

# End frequently toggled:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "PORT": config("DB_PORT", cast=int),
        "HOST": config("DB_HOST"),
        "TEST": {"NAME": config("TEST_DB_NAME")},
    }
}


# MAC
STATIC_URL = os.path.join(BASE_DIR, "static/")
# WINDOWS
# STATIC_URL = "/static/"

STATIC_ROOT = "static_dist"


if TEMPLATE_DEBUG:
    TEMPLATES[0]["OPTIONS"]["debug"] = True


SESSION_COOKIE_AGE = 9999999
SESSION_SECURITY_EXPIRE_AFTER = SESSION_COOKIE_AGE
SESSION_SECURITY_WARN_AFTER = SESSION_SECURITY_EXPIRE_AFTER - 100
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


ALLOWED_HOSTS = ["*"]


if ENABLE_TOOLBAR:
    INSTALLED_APPS += [
        "debug_toolbar",
        "graphiql_debug_toolbar",
    ]
    MIDDLEWARE += [
        # "debug_toolbar.middleware.DebugToolbarMiddleware"
        "graphiql_debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS = ["localhost", "127.0.0.1"]


if PRINT_ALL_DB_QUERIES:
    # warning: overwrites logging!
    LOGGING = {
        "version": 1,
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "django.db.backends": {
                "level": "DEBUG",
                "handlers": ["console"],
            }
        },
    }


SECRET_KEY = "7guqoosqau&1ryk*(uwa^_&vm_2bqldv4wk2fdcljv9uh$!-#="
