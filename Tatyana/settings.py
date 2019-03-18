"""
Django settings for Tatyana project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-v4a(7kig*dao5u)ym5b!2_n2zp#$mfy54cr&335xyw2h8&j)h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'website',
    'gallery',
    'users',
    'pages',
    'news',
    'experience',
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

ROOT_URLCONF = 'Tatyana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Tatyana.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_IMAGE_DIR = 'img/'
CONTENT_PICS_DIR = 'content/'
PROFILE_PHOTOS_DIR = 'photos/'
HEADER_PHOTOS_DIR = 'headers/'
GALLERY_PHOTOS_DIR = 'gallery/'
AWARDS_PHOTOS_DIR = 'awards/'
NEWS_PHOTOS_DIR = 'news/'
DOCUMENTS_DIR = 'documents/'
DOCUMENTS_MINIATURES_DIR = 'miniatures/'

CONTENT_PIC_DEFAULT_NAME = CONTENT_PICS_DIR + 'image.jpg'
PROFILE_PHOTO_DEFAULT_NAME = PROFILE_PHOTOS_DIR + 'profileimage.jpg'
HEADER_PHOTO_DEFAULT_NAME = HEADER_PHOTOS_DIR + 'header.jpg'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition
AUTH_USER_MODEL = 'users.User'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# CKEDITOR_CONFIGS по сути необязательны. Они влияют на тулбар редактора. Если выключите - будет очень мало
# инструментов для работы с текстом. После полной настройки - попробуйте с ними поиграться. Возможно найдете для себя
# какой-то более оптимальный вариант настроек!
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
             'RemoveFormat'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'sourcearea', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Maximize', 'ShowBlocks']
        ],
    }
}

PAGINATION_NEWS_ON_PAGE = 3  # Количество новостей на странице
PAGINATION_LIST_RANGE = 3  # Число страниц отопбажаемых в строке пагинация между "Назад" и "Вперед"

# Корневое меню
ABOUT = 'about'
GROUP = 'group'
DOCS = 'documents'
NEWS = 'news'
CONTACTS = 'contacts'
GALLERY = 'gallery'
PARENTS = 'parents'
METHODIC = 'methodic'

MENU_DEFAULT = ABOUT

MENU_CHOICES = (
    (ABOUT, 'обо мне'),
    (DOCS, 'документы'),
    (GROUP, 'группа'),
    (PARENTS, 'для родителей'),
    (METHODIC, 'мои разработки'),
    (NEWS, 'новости'),
    (GALLERY, 'фотогалерея'),
    (CONTACTS, 'контакты'),
)

# Награды
GRATEFUL = 'grateful'
LETTER = 'letter'
DIPLOM = 'diplom'
QUALIFICATION = 'qualification'
CERTIFICATE = 'certificate'

AWARDS_CHOICES = (
    (GRATEFUL, 'благодарность'),
    (LETTER, 'грамота'),
    (DIPLOM, 'диплом'),
    (QUALIFICATION, 'удостоверение'),
    (CERTIFICATE, 'сертификат'),
)

PDF = 'pdf'
PPT = 'ppt'
PPTX = 'pptx'
XLS = 'xls'
XLSX = 'xlsx'
DOC = 'doc'
DOCX = 'docx'
UNKNOWN = 'unknown'

DOCUMENT_TYPES = (
    (PDF, '*.pdf файл Adobe Reader'),
    (PPT, '*.ppt файл презентации MS PowerPoint 97/2003'),
    (PPTX, '*.pptx файл презентации MS PowerPoint'),
    (DOC, '*.doc текстовый файл MS Word 97/2003'),
    (DOCX, '*.docx текстовый файл MS Word'),
    (XLS, '*.xls файл электронных таблиц MS Excel 97/2003'),
    (XLSX, '*.xlsx файл электронных таблиц MS Excel'),
    (UNKNOWN, 'неизвестный тип файла'),
)

EDITOR = 'editor'
SPECIAL = 'special'

PAGE_TYPES = (
    (SPECIAL, 'Специализированная страница без выбора типа контента'),
    (DOCS, 'Страница с документами'),
    (EDITOR, 'Страница с редактированием текста')
)


# statics
NO_PHOTO = STATIC_IMAGE_DIR + 'nophoto.png'
DOCUMENT_PDF_MINIATURE = STATIC_IMAGE_DIR + 'pdf.png'
DOCUMENT_EXCEL_MINIATURE = STATIC_IMAGE_DIR + 'excel.png'
DOCUMENT_POWERPOINT_MINIATURE = STATIC_IMAGE_DIR + 'powerpoint.png'
DOCUMENT_WORD_MINIATURE = STATIC_IMAGE_DIR + 'word.png'
DOCUMENT_UNKNOWN_MINIATURE = STATIC_IMAGE_DIR + 'unknown.png'


# Виды шаблонов страниц
TEMPLATE_PAGE_DEFAULT = 'about.html'
TEMPLATE_DOCUMENTS = 'documents.html'
TEMPLATE_AWARDS = 'awards.html'
TEMPLATE_EDITOR = 'editor.html'
TEMPLATE_CONTACTS = 'contacts.html'
TEMPLATE_NO_PAGE = '404.html'


