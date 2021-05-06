import gnupg, os, glob, shutil
from pathlib import Path
from ftplib import FTP

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

# FTP Settings
FTPHost = "150.105.184.107"
FTPUser = "AARTIINDUSTRIE"
FTPPwd = "w0bo5qz9D0"
FTPPort = ""
FTPDir = "/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# PGP Settings
EmailKey = "jones.thayil@gmail.com"
KeyPhrase = 'Pass@123'
KeyType = "RSA"
KeyLen = "2048"
UserKey = "FTSPL Server"
Comment = "RSA 2048"
keyext = ('.key',)

# Auto-Key Management Program
if DEBUG:
    shutil.rmtree(keypath)
    os.makedirs(keypath)
    os.makedirs(pvtpath)
    os.makedirs(pubpath)
gpg = gnupg.GPG(gnupghome=keypath, verbose=False)
gpg.encoding = 'utf-8'

# Generate server fingerprint if not present
dirlen = len(os.listdir(pvtpath))
keycount = len(glob.glob1(exppath, "*.key"))
if dirlen > 1 and keycount > 1:
    if keycount < 2:
        key = gpg.list_keys(True)
    else:
        shutil.rmtree(pvtpath)
        os.makedirs(pvtpath)
        shutil.rmtree(pubpath)
        os.makedirs(pubpath)
else:
    input_data = gpg.gen_key_input(key_type=KeyType, key_length=KeyLen, name_real=UserKey, name_comment=Comment,
                                   name_email=EmailKey, passphrase=KeyPhrase)
    key = gpg.gen_key(input_data)
    shutil.rmtree(exppath)
    os.makedirs(exppath)
    ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
    with open(pubkey, 'w') as f:
        f.write(ascii_armored_public_keys)
S_fp = key.fingerprint
# if DEBUG: print("Key :\n", key)

# Getting client fingerprint if present
recipient = None
keycount = len(glob.glob1(imppath, "*.asc"))
if keycount == 1:
    for dirfiles in os.listdir(imppath):
        if dirfiles.endswith(".asc"):
            with open(imppath + '\\' + dirfiles, 'r') as file:
                f = file.read()
                imported_key = gpg.import_keys(f)
                gpg.trust_keys(gpg.list_keys()[1]['fingerprint'], 'TRUST_FULLY')
    if DEBUG: print(gpg.list_keys())
    C_fp = gpg.list_keys()[1]['fingerprint']
    if DEBUG: print(C_fp)
else:
    shutil.rmtree(imppath)
    os.makedirs(imppath)

# refresh media directory
shutil.rmtree(mediapath)
os.makedirs(mediapath)
