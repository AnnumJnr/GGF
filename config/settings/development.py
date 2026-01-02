"""
Development settings for GaGoForge.
"""

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='gagoforge_db'),
        'USER': config('DB_USER', default='gagomaster_user'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Development-specific settings
CORS_ALLOW_ALL_ORIGINS = True  # More permissive for development