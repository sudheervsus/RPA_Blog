import os

class BaseConfig(object):
    DEBUG = False
    Testing = False

class DevelopmentConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(64)
    DATABASE = 'database/rpablog.db'