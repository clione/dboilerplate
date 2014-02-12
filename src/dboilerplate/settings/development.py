import os

from defaults import *

####################################################
# Database settings (default: sqlite3)             #
####################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbboiler',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

####################################################
# Allowed hosts and security                       #
####################################################

ALLOWED_HOSTS = ['*']  # By default in development we allow any host

SECRET_KEY = 'v*&#e(xgw-fs1l#e%^nm-gqju(%hx@my@!9w^e08xyd(31cv90'


####################################################
# Internationalization                             #
####################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'


####################################################
# Email (default: deactivated)                     #
####################################################

#EMAIL_HOST = 'localhost'
#EMAIL_PORT= 25
#EMAIL_HOST_USER= ''
#EMAIL_HOST_PASSWORD= ''
#DEFAULT_FROM_EMAIL = ''
#EMAIL_USE_TLS = True


####################################################
# Caching (default: local cache)                   #
####################################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

####################################################
# Alerts                                           #
####################################################

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS


####################################################
# Fixtures (default: none)                         #
# Use this if you want to put test data in the DB  #
# on syncdb time                                   #
####################################################

FIXTURE_DIRS = (
    (BASE_DIR + '/fixtures/'),
)
