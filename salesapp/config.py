
import os
SECRET_KEY = os.urandom(32)
SECRET_KEY = SECRET_KEY
POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pw': os.getenv('POSTGRES_PASSWORD', 'password'),
    'db': os.getenv('POSTGRES_DB', 'sales'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', 5432),
}

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                        'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = False
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
