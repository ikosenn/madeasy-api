"""
Django settings for madeasy project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gz5+cmu50sky0j#yboon#ut7g8l$%ezo7ys@m=444*b(tthp_i'

# SECURITY WARNING: don't run with debug turned on in production!


def get_bool_env(env_var, default=False):
    assert default is False or default is True
    val = os.getenv(env_var, None)
    import json
    if val is None:
        return default
    try:
        p = json.loads(val)
        assert p is False or p is True
        return p
    except ValueError:
        raise Exception("Invalid boolean config: {}".format(val))

# ======== start sanity tests for get_bool_env ================


var1, default1 = 'tst-default-false', False
var2, default2 = 'tst-default-true', True

assert get_bool_env(var1, default1) is False
assert get_bool_env(var2, default2) is True

os.environ[var1] = 'false'
os.environ[var2] = 'false'
assert get_bool_env(var1, default1) is False
assert get_bool_env(var2, default2) is False

os.environ[var1] = 'true'
os.environ[var2] = 'true'
assert get_bool_env(var1, default1) is True
assert get_bool_env(var2, default2) is True

os.environ[var1] = 'some crap'
try:
    assert get_bool_env(var1, default1) is False
except Exception as ex:
    assert str(ex) == "Invalid boolean config: some crap"

os.environ[var1] = '"{}"'
try:
    assert get_bool_env(var1, default1) is False
except Exception as ae:
    assert isinstance(ae, AssertionError)
del os.environ[var1], os.environ[var2]
del var1, var2, default1, default2

# ======== end sanity tests for get_bool_env ==================


DEBUG = get_bool_env('DEBUG', True)

ALLOWED_HOSTS = ['.madeasy.io', '.localhost']
CORS_ORIGIN_REGEX_WHITELIST = (
    '^(https?://)?(\w+\.)?localhost\:8030$',
    '^(https?://)?(.+)-?.madeasy.io$',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'corsheaders',
    'rest_framework',
    'mptt',
    # 'rest_auth',
    'madeasy.data_bootstrap',
    'madeasy.common',
    'madeasy.madeasy_auth',
    'madeasy.airline',
    'madeasy.booking',
    'madeasy.payment',
    'madeasy.parser',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'madeasy.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'madeasy.config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
db_url = 'postgres://madeasy_user:madeasy@localhost:5432/madeasy'

DATABASES = {'default': dj_database_url.config(env='blahblah', default=db_url)}
DATABASES['default']['CONN_MAX_AGE'] = 60

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': (
        'rest_framework.serializers.ModelSerializer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # Pagination settings
    'PAGE_SIZE': 30,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 15000,

    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.MultiPartRenderer',
    ),

    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601',
}


OAUTH2_PROVIDER_APPLICATION_MODEL = 'madeasy_auth.OauthApplication'
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'madeasy_auth.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


if (os.path.exists('/dev/log')):
    sock_handler = '/dev/log'
else:
    sock_handler = '/var/run/syslog'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] " +
                      "%(module)s %(process)d %(thread)d %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': sock_handler,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['syslog', 'console'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['syslog', 'console'],
            'propagate': False,
            'level': 'ERROR',
            'filters': ['require_debug_false'],
        },
        'django.db': {
            'handlers': ['syslog', 'console'],
            'propagate': False,
            'level': 'ERROR',
            'filters': ['require_debug_false'],
        },
        'madeasy': {
            'handlers': ['syslog', 'console'],
            'level': 'DEBUG',
        },
    }}


# add HSTS on the backend requests for a dynamic
# period of 1 year on all project subdomains
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

if os.getenv('HTTPS_ENABLED'):
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


CSRF_COOKIE_AGE = None
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
