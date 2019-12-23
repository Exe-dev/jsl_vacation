from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, r'C:\Users\tooka\Documents\jsl_vacation\jsl_vacation\db.sqlite3'),
    }
}

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['string_if_invalid'] = 'Invalid Variable: %s'
