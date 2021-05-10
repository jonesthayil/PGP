import gnupg, os, glob, shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
rootpath = str(BASE_DIR)
# Server Key Directory
keypath = rootpath + '\\gnupg'
pvtpath = keypath + '\\private-keys-v1.d'
pubpath = keypath + '\\openpgp-revocs.d'
# Public Key Backups for In,Ex-port
imppath = rootpath + '\\import_key'
exppath = rootpath + '\\export_key'
pubkey = exppath + '\\pub_key.asc'
# Encrypt file location
mediapath = rootpath + '\\media'

SECRET_KEY = 'django-insecure-cp(f5f=-om-0@sgb!5xaa-!sn1^(xtagl4bdn01o3-6lx=-#pw'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ftcrypt.apps.FtcryptConfig',
    'rest_framework',
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

ROOT_URLCONF = 'ftspl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ftspl.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

gpg = gnupg.GPG(gnupghome=keypath, verbose=False)
gpg.encoding = 'utf-8'

# Importing client keys from import_key folder
with open(imppath + '\\CITI_public_key_CPGP_GXS_2048_20221208.asc', 'r') as file:
    f = file.read()
    imported_key = gpg.import_keys(f)
    gpg.trust_keys(gpg.list_keys()[0]['fingerprint'], 'TRUST_FULLY')
    print(gpg.list_keys()[0]['fingerprint'])
    C_fp = gpg.list_keys()[0]['fingerprint']

# Importing server keys from export_key folder
with open(exppath + '\\pgp_private_key.asc', 'r') as file:
    f = file.read()
    imported_key = gpg.import_keys(f)
    gpg.trust_keys(gpg.list_keys()[1]['fingerprint'], 'TRUST_FULLY')
    print(gpg.list_keys()[1]['fingerprint'])
    S_fp = gpg.list_keys()[1]['fingerprint']
