import os
from dspace.settings import SECRET_KEY, INSTALLED_APPS, ROOT_URLCONF

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_space',
  }
}