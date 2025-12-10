"""
"""
"""
Django settings for config project. (Versión Edulider 0)
...
"""

import os
from pathlib import Path
import dj_database_url # Añadido para manejar la DATABASE_URL de Railway

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 1. SECRET_KEY: OBLIGATORIO usar variable de entorno en producción (Railway).
# El valor de fallback es solo para desarrollo local.
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '#j89)yo9qfra6^-c7hztfkk^8zf*v2nr_=!*t6b!6*a*$msn_2' # Clave temporal de desarrollo
)

# 2. DEBUG: Siempre False en producción para evitar exponer información sensible.
# Solo True si la variable de entorno 'DJANGO_DEBUG' está explícitamente en 'True'.
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'


# 3. ALLOWED_HOSTS: Manejo condicional para desarrollo y producción.
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')

if DEBUG:
    # En desarrollo local: permite localhost y 127.0.0.1
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
elif ALLOWED_HOSTS_ENV:
    # En producción: usa la lista provista por la variable de entorno.
    ALLOWED_HOSTS = ALLOWED_HOSTS_ENV.split(',')
else:
    # Producción segura: si DEBUG es False y no hay variable, lista vacía.
    ALLOWED_HOSTS = []


# Application definition
# ... (El resto de INSTALLED_APPS, MIDDLEWARE, ROOT_URLCONF, TEMPLATES permanece igual) ...


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Conexión a Base de Datos (PostgreSQL en Railway)
# Leer la variable de entorno DATABASE_URL proporcionada por Railway
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Si la variable existe (entorno Railway): usa PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True # Crucial para conexiones seguras con PostgreSQL en la nube
        )
    }
else:
    # Si la variable no existe (desarrollo local): usa SQLite por defecto
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# ... (El resto del código permanece igual) ...

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
