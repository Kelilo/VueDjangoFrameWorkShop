# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/12 0012 22:07'

# 云片网设置
APIKEY = 'd6c4ddbf50ab36611d2f52041a0b949e'

# sentry的设置
import os
import raven


# RAVEN_CONFIG = {
#     'dsn': 'http://ad429813913e4071ab33a6e70d31e37b:346631d638cd49c3b8c0ee6186838938@115.159.122.64:9000//2',
# }

# 第三方登录
SOCIAL_AUTH_WEIBO_KEY = '4117332009'
SOCIAL_AUTH_WEIBO_SECRET = '9c21c82d76ec8c5af4e4a87e3d30b6fa'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'

SOCIAL_AUTH_QQ_KEY = '101467908'
SOCIAL_AUTH_QQ_SECRET = 'a5c4f2d99f952430251f7c40f4fa5c3b'

SOCIAL_AUTH_WEIXIN_KEY = 'foobar'
SOCIAL_AUTH_WEIXIN_SECRET = 'bazqux'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vue_shop',
        'USER': 'root',
        'PASSWORD': 'mtianyanmysql',
        'HOST': '139.199.189.211',
        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}
    }
}

