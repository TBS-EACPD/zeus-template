from decouple import Csv, config

from .base import *

DEBUG_FORM_FIELDS = False
DEBUG = False

SESSION_COOKIE_AGE = 1800  # 30 min
SESSION_SECURITY_EXPIRE_AFTER = SESSION_COOKIE_AGE
SESSION_SECURITY_WARN_AFTER = SESSION_SECURITY_EXPIRE_AFTER - 100
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


TEMPLATES[0]["OPTIONS"]["debug"] = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

SECRET_KEY = config("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "PORT": config("DB_PORT", cast=int),
        "HOST": config("DB_HOST"),
        "OPTIONS": {"sslmode": "verify-ca", "sslrootcert": "./ca-certificate.crt"},
    }
}


STATIC_URL = "/static_dist/"
STATIC_ROOT = "static_dist"


SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_HSTS_SECONDS = 31536000  # - One Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

