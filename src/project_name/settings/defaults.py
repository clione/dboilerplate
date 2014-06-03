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
    'yawdadmin',                   # Load yawdadmin first
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
)

APPS = (
    'apps.managecommands',
)

THIRDPARTY_APPS = (
    'allauth',                                   # General AllAuth stuff
    'allauth.account',                           # Database authentication
    'allauth.socialaccount',                     # Social auth abilities
    'allauth.socialaccount.providers.facebook',  # Facebook auth
    'allauth.socialaccount.providers.google',    # Google auth
    # For extra authentication mechanisms please check the allauth docs
    # website: http://django-allauth.readthedocs.org/en/latest/

     'south',
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + APPS


####################################################
# Middleware and handlers                          #
####################################################

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    # Yawd middlweware, it shouldn't be required in django 1.6+ but it still
    # asks for it
    'yawdadmin.middleware.PopupMiddleware',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB in RAM for the uploads

####################################################
# Administration panel details                     #
####################################################

# Yawn admin
ADMIN_SITE_NAME = 'Tip Exchange 1.3 Administration'
ADMIN_SITE_DESCRIPTION = "Where there's a stain, there's a way."

####################################################
# Messaging (also know as django messages)         #
####################################################

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

####################################################
# Authentication                                   #
####################################################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    "allauth.account.auth_backends.AuthenticationBackend",  # Allauth
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

    # Allauth
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
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

LOCALE_PATHS = (
    BASE_DIR + '/locale',
)

#######################################################
# Webfont mime type fix for firefox and safari
#######################################################

import mimetypes
mimetypes.add_type("application/font-woff", ".woff", True)

####################################################
# Static and uploads urls and paths                #
####################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/static'))
MEDIA_URL = ''
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/media'))

BUILD_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../../htdocs/build_output'))

STATICFILES_DIRS = (
    BUILD_ROOT,
)

####################################################
# Other settings                                   #
####################################################

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
SITE_ID = 1

##########################################################
# Allauth settings                                       #
# Docs: http://django-allauth.readthedocs.org/en/latest/ #
##########################################################

ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True  # Must be true if auth is with email
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_BLACKLIST = ['root', 'penis', 'cunt', 'stupid', 'password']
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_MIN_LENGTH = 4
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# This setting will try to get the data directly from the social account to
# bypass the signup form. If there is some error the form still will appear
SOCIALACCOUNT_AUTO_SIGNUP = True
# Specific settings for the social authentication if required
SOCIALACCOUNT_PROVIDERS = {}

SOCIALACCOUNT_PROVIDERS = \
    {'facebook': {
        'VERIFIED_EMAIL': True}}  # Prevent allauth of asking to confirm email

####################################################
# Logging                                          #
####################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },

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
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/django.log",
            'maxBytes': 2097152,  # 2MB per file
            'backupCount': 2,  # Store up to three files
            'formatter': 'standard',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Log all the things!
        '': {
            'handlers': ["logfile", ],
            'level': 'DEBUG',
        },
    }
}
