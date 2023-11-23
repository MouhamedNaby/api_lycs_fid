"""
Django settings for lycsfid project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
# importation de config
from decouple import config
#importation database-url
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}
# Application definition

INSTALLED_APPS = [
     'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api_lycs_fid.apps.ApiLycsFidConfig',
    'drf_yasg',
    "corsheaders",
    'rest_framework',
    'rest_framework_simplejwt',
     'utils',
]
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=7),
    'SLIDING_TOKEN_REFRESH_LEEWAY': timedelta(days=0),
    'SLIDING_TOKEN_LEEWAY': timedelta(days=0),
    'SLIDING_TOKEN_TYPES': ('access', 'refresh'),
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_SLIDING_EXP_CLAIM': 'sliding_exp',
    'SLIDING_TOKEN_REFRESH_SLIDING_EXP_CLAIM': 'refresh_sliding_exp',
    'SLIDING_TOKEN_USER_ID_CLAIM': 'user_id',
    'SLIDING_TOKEN_USERNAME_CLAIM': 'email',
    'SLIDING_TOKEN_LAST_LOGIN_CLAIM': 'last_login',
    'SLIDING_TOKEN_COOKIE': 'jwt',
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lycsfid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'lycsfid.wsgi.application'


# SERVER DATABASE
DATABASES ={
    'default':dj_database_url.parse(config('DATABASE_URL'))
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test',
#         'USER': 'postgres',
#         'PASSWORD': 'LycsDakar@23',
#         'HOST': 'localhost',  # Laissez vide pour utiliser le localhost
#         'PORT': '5432',  # Laissez vide pour utiliser le port par défaut (5432)
#     }
# }


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nabipulo@gmail.com'
EMAIL_HOST_PASSWORD = 'cosqnimydglosxug'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL= False

PASSWORD_RESET_TIMEOUT = 14400
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
AUTH_USER_MODEL = 'api_lycs_fid.User'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') #le chemin du serveur pour stocker les fichiers sur l’ordinateur. 
MEDIA_URL = '/media/'# comment l’URL de référence permettant au navigateur d’accéder aux fichiers via Http.
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#CORS_ALLOWED_ORIGINS = ["http://localhost:4200", "http://127.0.0.1:4200","http://127.0.0.1:4200","http://127.0.0.1","https://lycsfid.onrender.com"]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-csrf-token",
    "csrftoken",
    "x-requested-with",
    "http_x_csrftoken"
    'access-control-allow-origin',
    'access-control-allow-credentials',
    'mode'
]
ALLOWED_HOSTS=['*']
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True