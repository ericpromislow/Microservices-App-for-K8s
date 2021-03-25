import secrets
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_hex(32))
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    PRODUCTS_PER_PAGE = 20
    CUSTOMERS_PER_PAGE = 50
    ORDERS_PER_PAGE = 50
    SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SOCKSESS_DB", 'sqlite+pysqlite:///' + os.path.join(basedir, 'myorders.db'))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SOCKSESS_DB", 'sqlite+pysqlite:///' + os.path.join(basedir, 'testing.db'))
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SOCKSESS_DB', 'postgresql://socksess:socksess@localhost:5432/socksess')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
