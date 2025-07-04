"""
Django settings for GramiSys project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import vistaprevia
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j0&8#r62ct#w01j0trjkj5obhog9o!v#%#7+urn#aix#gylxn4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application por definicion

INSTALLED_APPS = [
    
    #agregando lineas para el registro redux
    'django.contrib.sites',
    'registration',
    'debug_toolbar', # para debug
    
    #app por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps terceros

    'captcha',

    #mis apps
    'vistaprevia.apps.VistapreviaConfig',
    'usuarios.apps.UsuariosConfig',
    'productos.apps.ProductosConfig',
    'contacto.apps.ContactoConfig',
    'tienda.apps.TiendaConfig',
    

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

ROOT_URLCONF = 'GramiSys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], #todas mis vistas se tienen que mostrar en templates que las busque 
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

WSGI_APPLICATION = 'GramiSys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False #True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/' 

# dentro de la carpeta static_dev vamos a poner imagenes estaticas, diseños fijos, animacion
#agregadas desde el doc del prfe

# static solo a produccion dev si lo que dije arribe
#media graficos, videos, imagenes q muestren 

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL= '/' #una vez que te registres va a esta url
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL= '/accounts/login/'
REGISTRATION_SUCCESS_URL = '/accounts/login/'  # A dónde querés ir después de registrarte
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#la persona tiene 7 dias para logearse o se borra
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN= True
SITE_ID= 1 #cuantos sitios estamos usando. usamos solo 1

 #COPIO CODE DE PROFE PARA EL DEBUG
if DEBUG:
    MIDDLEWARE +=[

        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    INTERNAL_IPS= [
        "127.0.0.1",
    ]

    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True) 

    DEBUG_TOOLBAR_CONFIG={
        "INTERCEP_REDIRECTS": False,
    }

