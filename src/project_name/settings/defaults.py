"""
Default settings for the project. All the common settings to all the
environments should be here, like applications.
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


####################################################
# Applications                                     #
####################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
)

APPS = ()

THIRDPARTY_APPS = (
     'south',
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + APPS


####################################################
# Middleware and handlers                          #
####################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)


####################################################
# Messaging (also know as django messages)         #
####################################################

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


####################################################
# Authentication                                   #
####################################################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
)


####################################################
# Templating                                       #
####################################################

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    (BASE_DIR + '/templates'),
)


####################################################
# Internationalization                             #
####################################################

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en_GB', 'English'),
)

####################################################
# Static and uploads urls and paths                #
####################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/static'))
MEDIA_URL = ''
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/media'))

BUILD_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../build_output'))

STATICFILES_DIRS = (
    BUILD_ROOT,
)

####################################################
# Other settings                                   #
####################################################

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


####################################################
# Logging                                          #
####################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
