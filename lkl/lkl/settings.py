# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'be5k77)sb&c4$=bj05(u=yqcrjsg9=%2=mnst6r2&v0)ma5sck'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'lkl',
    'admin_view_permission',
    'suit',
    'easy_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "raven.contrib.django.raven_compat",
    'captcha',
    'user',
    "xyf",
    "jinkong"
]

ADMIN_VIEW_PERMISSION_MODELS = [
    'auth.User',
    'user.UserProfile',
    'user.UserAddress',
    'user.UserPos',
    'user.UserTrade',
    'user.LKLTrade01',
    'user.UserFenRun',
    'user.LKLTerminal',
    'user.LKLD0',
    'user.LKLD1',
    'user.UserRMB',
    'user.ProfitD1',
    'user.ProfitD0',
    'user.ChildProfitD1',
    'user.ChildProfitD0',
    'user.TiXianOrder',
    'user.UserAlipay',
    'user.FenRunOrder',
    'user.SLKLToken',
    "xyf.XYFToken",
    "xyf.SYFTrade",
    "xyf.SYFTerminal",
    "xyf.XYFPos",
    "xyf.XYFFenRun",
    "xyf.XYFUserRMB",
    "xyf.XYFProfit",
    "xyf.XYFTiXianOrder",
    "jinkong.JKMerchant",
    "jinkong.JKTerminal",
    "jinkong.JKTrade",
    "jinkong.JKSettlement",
    "jinkong.JKPos",
    "jinkong.JKFenRun",
    "jinkong.JKYunFenRun",
    "jinkong.JKUserRMB",
    "jinkong.JKProfit",
    "jinkong.JKChildProfit",
    "jinkong.JKTiXianOrder",
    "jinkong.JKToken"
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

ROOT_URLCONF = 'lkl.urls'

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

WSGI_APPLICATION = 'lkl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
TIME_FORMAT = "H:i:s"
DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i:s"

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s:%(lineno)d:: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'statistics': {
            'format': '%(asctime)s | %(levelname)s | %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s] - %(message)s'
        },
        'record': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': "/var/log/lakala/debug.log",
            'level': 'ERROR',
        },
        'statistics_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'statistics',
            'filename': "/var/log/lakala/statistics.log",
            'level': 'DEBUG',
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['mail_admins', "file"],
            'level': 'ERROR',
            'propagate': True,
        },
        'statistics': {
            'handlers': ['statistics_handler'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = '/user/login/'
LOGOUT_URL = '/user/logout/'
LOGIN_REDIRECT_URL = '/user/'

# for suit
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'营销平台',
    'HEADER_DATE_FORMAT': DATE_FORMAT,
    # 'HEADER_TIME_FORMAT': TIME_FORMAT,

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'SEARCH_URL': '',
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU': (
        # 'sites',
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'app': 'user', 'icon': 'icon-user', 'models': ('UserProfile', 'UserAddress', 'UserPos', 'UserTrade', "UserFenRun", "UserAlipay")},
        {'label': u'微信用户', 'icon': 'icon-user', 'app': 'user', 'models': ('WXUser', )},
        # lkl
        # {'label': u'刷卡数据', 'icon': 'icon-star-empty', 'app': 'user', 'models': ('LKLTrade01', )},
        # {'label': u'刷卡数据(老系统)', 'icon': 'icon-star', 'app': 'user', 'models': ('LKLTerminal', 'LKLD0', 'LKLD1')},
        # {'label': u'用户分红', 'icon': 'icon-gift', 'app': 'user', 'models': ('UserRMB', 'ProfitD1', 'ProfitD0', 'ChildProfitD1', 'ChildProfitD0')},
        # {'label': u'审核管理', 'icon': 'icon-check', 'app': 'user', 'models': ('TiXianOrder', 'FenRunOrder')},
        # {'label': u'拉卡拉官网', 'icon': 'icon-globe', 'blank': True,
        #     'models': (
        #         {'label': u'新系统', 'icon': 'icon-star', 'url': 'https://mposa.lakala.com/', 'blank': True},
        #         {'label': u'老系统', 'icon': 'icon-star', 'url': 'https://s.lakala.com/', 'blank': True},
        #     )
        # },
        # {'label': u'营收状况', 'icon': 'icon-heart', 'url': 'admin_income', 'blank': False},
        # {'label': u'去催单', 'icon': 'icon-plane', 'url': 'admin_reminder', 'blank': False},
        # {'label': u'卡拉慧', 'icon': 'icon-flag', 'url': 'user_home', 'blank': True},
        # {'label': u'TOKEN', 'icon': 'icon-check', 'app': 'user', 'models': ('SLKLToken',)},
        {'label': u'星驿付数据', 'icon': 'icon-star', 'app': 'xyf', 'models': ('SYFTerminal', 'SYFTrade', 'XYFToken', 'XYFPos', 'XYFFenRun', 'XYFUserRMB', 'XYFProfit', 'XYFTiXianOrder')},
        {'label': u'金控数据', 'icon': 'icon-heart', 'app': 'jinkong', 'models': ('JKMerchant', 'JKTerminal', 'JKTrade', 'JKSettlement', 'JKPos', 'JKFenRun', 'JKYunFenRun', 'JKToken')},
        {'label': u'金控金钱', 'icon': 'icon-heart', 'app': 'jinkong', 'models': ('JKUserRMB', 'JKProfit', 'JKChildProfit', 'JKTiXianOrder')},
        {'label': u'金控营收状况', 'icon': 'icon-heart', 'url': 'admin_jk_income', 'blank': False},
    ),

    # misc
    'LIST_PER_PAGE': 20
}
