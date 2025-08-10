# PORTAL_ADMIN/adminportal/mysite/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta # Se estiver usando timedelta, mantenha
import psycopg2 # Se estiver usando psycopg2 diretamente, mantenha
from django.core.exceptions import ImproperlyConfigured # Adicione este import

# Carregamento de variáveis de ambiente
# A linha abaixo foi ajustada para carregar o .env da raiz do projeto (PORTAL_ADMIN/)
# Se o seu .env estiver em outro local, ajuste o caminho conforme necessário.
load_dotenv(Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).parent / '.env')

# Chave de criptografia para campos customizados
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY and not settings.DEBUG:
    raise ImproperlyConfigured("ENCRYPTION_KEY must be set in production.")

# Certifique-se que o cache esteja configurado para a função get_credential
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
# MinIO Configuration
# MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
# MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
# MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
# # Converta a string 'True' ou 'False' para booleano
# MINIO_SECURE = os.getenv("MINIO_SECURE", 'False').lower() == 'true'
# MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")

# # ASSEMBLYAI Configuration
# ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# WEBHOOK_N8N = os.getenv("WEBHOOK_N8N")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w_hi$f!)+j@km=4^a(rdscb$9rr8j12eg@)k$8jh==n0vu(l51'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Adicione o novo domínio do seu túnel de desenvolvimento aqui
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '7lxwl92c-8000.brs.devtunnels.ms', # Removido a barra final para consistência, embora Django geralmente lide com isso
    '0.0.0.0', # <--- ADICIONE ESTA LINHA PARA RESOLVER O ERRO DisallowedHost
]

# Application definition

INSTALLED_APPS = [
    'meu_app.apps.PollsConfig', # Use apenas esta linha para o seu aplicativo 'meu_app'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Deve vir antes de CommonMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo' # Ou 'UTC' se preferir
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Adicione esta configuração para que collectstatic encontre os arquivos estáticos
STATICFILES_DIRS = [
    # Caminho para os arquivos estáticos do Django Admin
    os.path.join(BASE_DIR, '..', '.venv', 'lib', 'python3.12', 'site-packages', 'django', 'contrib', 'admin', 'static'),
    # Caminho para os arquivos estáticos do Django REST Framework
    os.path.join(BASE_DIR, '..', '.venv', 'lib', 'python3.12', 'site-packages', 'rest_framework', 'static'),
    # Se você tiver arquivos estáticos no seu app 'meu_app/static/', eles já devem ser encontrados
    # caso contrário, adicione: os.path.join(BASE_DIR, 'meu_app', 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Configurações CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://7lxwl92c-8000.brs.devtunnels.ms", # Removido a barra final para consistência
    "http://0.0.0.0:8000",
    # "http://localhost:8000",# <--- ADICIONE ESTA LINHA COM O ESQUEMA
]
# CORS_ALLOW_ALL_ORIGINS = True # Remova ou comente esta linha em produção

# Adicione esta linha para confiar no localhost para CSRF quando DEBUG=False
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://7lxwl92c-8000.brs.devtunnels.ms", # Removido a barra final para consistência
    "http://0.0.0.0:8000", # <--- ADICIONE ESTA LINHA COM O ESQUEMA
]


# URL para redirecionamento após login (se você tiver uma view de perfil)
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/' # Opcional: URL para redirecionar após logout
