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


# Model Constants
# -----------------------------------------------------------------------------
class ModelConstants(Enum):
    """model constants"""

    USERS = "users"
    CHOICES = "choices"


# Templates Path Constants
# -----------------------------------------------------------------------------
class Templates(Enum):
    """Template paths constants"""

    INDEX = "polls_api/index.html"
    ABOUT = "polls_api/about.html"
    DEMO = "demo/index.html"


# Urls & Url Reverse Constants
# -----------------------------------------------------------------------------
class Urls(Enum):
    INDEX = "index"
    ABOUT = "about"
    USERS = "users"
    CHOICES = "choices"
    DEMO = "demo"


# Other Constants
# -----------------------------------------------------------------------------
EMPTY_STR = ""
FORM_CLASS = "input input-bordered w-full"
FORM_CLASS_FILE = "file-input file-input-bordered w-full"
TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
SELECT_CLASS = "select select-bordered w-full select-sm"
THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
    ("cmyk", "cmyk"),
    ("autumn", "autumn"),
    ("business", "business"),
    ("acid", "acid"),
    ("lemonade", "lemonade"),
    ("night", "night"),
    ("coffee", "coffee"),
    ("winter", "winter"),
    ("dim", "dim"),
    ("nord", "nord"),
    ("sunset", "sunset"),
)
