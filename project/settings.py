import os
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '28$93@150+tqvgapo2z#5!+p--n6^)r+f1jn$2x9nu3r_u59mq'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'adminlte3',

    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'parler',
    'rosetta',
    'cabinet',
    'imagefield',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    # 'captcha',
    'mptt',
    'mapbox_location_field',

    'blogs.apps.BlogsConfig',
    'users.apps.UsersConfig',

    'active_link',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # for context
                'project.context.defaults',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

AUTH_USER_MODEL = "users.User"

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.postgresql',
# 		'NAME': 'uzcharm2',
# 		'USER': 'postgres',
# 		'PASSWORD': 'ubuntu',
# 		'HOST': 'localhost',
# 		'PORT': '5432',
# 	}
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tashkent'

ADMIN_UI_LOCALE = 'ru'

PARLER_DEFAULT_LANGUAGE_CODE = 'ru'

USE_I18N = True

USE_L10N = True

USE_TZ = False

CABINET_FILE_MODEL = 'yourapp.File'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'project/static'),
    os.path.join(BASE_DIR, 'staticfiles'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LANGUAGES = (
    ('uz', 'O\'zbek'),
    ('en', 'English'),
    ('ru', 'Русский'),
)

PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE

PARLER_ENABLE_CACHING = False

PARLER_LANGUAGES = {
    None: (
        {'code': 'uz'},
        {'code': 'en'},
        {'code': 'ru'},
    ),
    'default': {
        'fallback': 'en',  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    }
}

ROSETTA_AUTO_COMPILE = True

MAPBOX_KEY = 'pk.eyJ1IjoiYWZ6YWwteXVzdXBvdiIsImEiOiJja2xrcDVvMWwyaHM1MnBwN2RvdHoxZngyIn0.JauSJzmB9GXloPrr8cP8Fw'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_HOST_USER = 'yusupovafzal@gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_SSL = True

CONTACT_EMAIL = 'afzal-yusupov@mail.ru'
ADMIN_EMAIL = ['admin@example.com', ]

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'

MESSAGE_TAGS = {
    messages.ERROR: "danger"
}


ACTIVE_LINK_CSS_CLASS = "active"


def rosetta_user(user, *args, **kwargs):
    if user.is_superuser:
        return True
    else:
        return False

ROSETTA_ACCESS_CONTROL_FUNCTION = rosetta_user


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
