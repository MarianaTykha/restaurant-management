from .base import *

DEBUG = False

ALLOWED_HOSTS = ["restaurant-management.onrender.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": int(os.getenv("POSTGRES_DB_PORT", 5432)),
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}
