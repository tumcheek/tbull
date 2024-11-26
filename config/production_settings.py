from .base_settings import *

DEBUG = False
WEBSITE_DOMAIN = getenv("WEBSITE_DOMAIN")
ALLOWED_HOSTS = [WEBSITE_DOMAIN, f"www.{WEBSITE_DOMAIN}"]
