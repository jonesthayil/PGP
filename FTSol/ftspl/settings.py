from pathlib import Path
from ftplib import FTP
import gnupg

BASE_DIR = Path(__file__).resolve().parent.parent

rootpath = str(BASE_DIR)

keypath = rootpath + '\gnupg'

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

# PGP Settings
Email = 'jones.thayil@gmail.com'
Passkey = 'Pass@123'
Type = 'RSA'
Length = '1024'

# FTP Settings
ftp = ''
'''
ftp = FTP("46.17.172.192")
ftp.login(user='u399571136.maulisaidevelopers.com', passwd='Pass@123')
# ftp.cwd('/www/')
'''

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

gpg = gnupg.GPG(gnupghome=keypath)


def generatekey(Email, Passkey, Type, Length):
    gpg.encoding = 'utf-8'
    input_data = gpg.gen_key_input(
        name_email=Email,
        passphrase=Passkey,
        key_type=Type,
        key_length=Length,
    )
    newkey = gpg.gen_key(input_data)
    print(str(newkey))


# generatekey(Email, Passkey, Type, Length)
