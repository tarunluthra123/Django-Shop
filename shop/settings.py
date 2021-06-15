from datetime import timedelta
from pathlib import Path

import environ
import django_heroku


env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-af35a!6+9ic+$l1ort&!zlj&+)%0_+#_1xxdoag9+sd79_rkqc'

DEBUG = True

ALLOWED_HOSTS = [
    "*"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'api',
    'django_s3_storage',
    
    'coreapi', # Coreapi for coreapi documentation
    'drf_yasg', # drf_yasg fro Swagger documentation
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('AWS_DB_NAME'),
        'USER': env('AWS_DB_USERNAME'),
        'PASSWORD': env('AWS_DB_PASSWORD'),
        'HOST': env('AWS_DB_HOST'),
        'PORT': env('AWS_DB_PORT')
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# JWT Auth
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'ALGORITHM': 'HS512',
    'SIGNING_KEY': env('JWT_SECRET_KEY')
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'

# AWS Settings
# The AWS region to connect to.
AWS_REGION = "ap-south-1"

# The AWS access key to use.
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')

# The AWS secret access key to use.
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

# The name of the bucket to store files in.
AWS_S3_BUCKET_NAME = "django-shop-images-bucket"

# AWS Static Files
AWS_S3_BUCKET_NAME_STATIC = 'django-shop-images-bucket'

django_heroku.settings(locals())