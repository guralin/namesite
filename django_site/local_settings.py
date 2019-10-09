from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LOGGING = {
    # バージョンは「１」固定
    'version' : 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers' : False,
    # ログフォーマット
    'formatters': {
        # 本番用
        'production': {
            'format' : '%(asctime)s [%(levelname)s] %(process)d %(thread)d'
                        '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    # ハンドラ
    'handlers':{
        # ファイル出力用ハンドラ
        'file' : {
            'level':'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'formatter': 'production',
        },
    },
    'loggers': {
        # 自作アプリケーション全般のログを拾うロガー
        '' : {
            'handlers' : ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'django' : {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
