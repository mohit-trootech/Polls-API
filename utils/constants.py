from enum import Enum
from dotenv import dotenv_values

config = dotenv_values(".env")


# Settings Constants
# -----------------------------------------------------------------------------
class Settings(Enum):
    ROOT_URL = "polls_api.urls"
    TEMPLATE = "templates"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG_TOOLBAR_IP = "127.0.0.1"
    CACHE_TABLE_NAME = "cache_table"
    SECRET_KEY = config.get("SECRET_KEY")


# Email Configurations
# -----------------------------------------------------------------------------
class EmailConfig(Enum):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587
    EMAIL_HOST_USER = config.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config.get("EMAIL_HOST_PASSWORD")
