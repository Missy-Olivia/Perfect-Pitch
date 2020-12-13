import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class TestConfig(Config):


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}