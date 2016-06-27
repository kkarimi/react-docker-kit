import os

DEBUG = True

env = os.environ

HOST = env.get("HOST", "0.0.0.0")
PORT = env.get("PORT", "5000")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CELERY_BROKER_URL = env.get("CELERY_BROKER_URL", "redis://localhost:6379"),
CELERY_RESULT_BACKEND = env.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

CORS_HEADERS = "Content-Type"
