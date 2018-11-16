from app.settings.base import *


###ENV settings
# SECURITY WARNING: don't run with debug turned on in production!
ENVIRONMENT = 'development'
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    # central db (users, companies)
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    },
}

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(PROJECT_DIR,'static/')
