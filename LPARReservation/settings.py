"""
Django settings for LPARReservation project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yj+!x(y&w)by=t%cq)xoy(pl7n-q^57(qr*hr!pr=d*8ezvx5r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']
DATABASES = { 
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'lpardb',
        'USER': 'django_user',
        'PASSWORD': 'passw0rd',
        'HOST': 'localhost',
        #'PORT': '',
    }   
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_openid_auth',
    'LPARReservation',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'LPARReservation.urls'

WSGI_APPLICATION = 'LPARReservation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

SITE_ID = "1"

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin'

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'

OPENID_SSO_SERVER_URL = "https://w3-03.sso.ibm.com/FIM/openidsso"
OPENID_TRUST_ROOT = "https://9.115.122.85"
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
