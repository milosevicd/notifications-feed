import logging

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXPLAIN_TEMPLATE_LOADING = True
    LOG_LEVEL = logging.INFO


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@host/db-name" # TODO externalize this


class DevelopmentConfig(Config):
    LOG_LEVEL = logging.DEBUG
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://" # in-memory database for development
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://" # in-memory database for testing
    SQLALCHEMY_ECHO = False
