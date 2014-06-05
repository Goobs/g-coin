# -*- coding: utf-8 -*-

from .base import *

SECRET_KEY = '5&2b5$!3)!%#c3bz%@h2p&ac$vo1e7*ivap5_a1l-c)mya7b6z'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ('localhost', )


