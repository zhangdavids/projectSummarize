# -*- coding: utf-8 -*-


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """ 配置基类 """

    DEBUG = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = ''
    FLASK_MAIL_SENDER = ''
    FLASK_MAIL_ADMIN = ''

    @staticmethod
    def __init__(app):
        pass


class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = True
    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_TLS = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'db', 'development.sqlite')


class ProductionConfig(BaseConfig):
    """ 成产环境配置 """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'db', 'data.sqlite')


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'db', 'testing.sqlite')


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig,
}
