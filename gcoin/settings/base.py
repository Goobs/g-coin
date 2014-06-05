# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gcoin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gcoin.urls'
WSGI_APPLICATION = 'gcoin.wsgi.application'

GRAPPELLI_ADMIN_TITLE = 'Agora'
GRAPPELLI_INDEX_DASHBOARD = 'agora.admin.dashboard.IndexDashboard'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

FEINCMS_RICHTEXT_INIT_TEMPLATE = 'admin/content/richtext/init_tinymce4.html'
FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': STATIC_URL + 'cms/tinymce/tinymce.min.js',
}


from django.contrib.messages import constants
MESSAGE_TAGS = {
    constants.ERROR: 'danger',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

