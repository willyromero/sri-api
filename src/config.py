from decouple import config

class BaseConfig(object):
    APPLICATION_ROOT = "/"
    JSON_AS_ASCII = False
    SECRET_KEY = config("SECRET_KEY")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SERVER_NAME = config("DEV_SERVER_NAME")

class ProductionConfig(BaseConfig):
    DEBUG = False
    SERVER_NAME = config("SERVER_NAME")