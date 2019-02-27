import os

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "dbname='test_db' user='postgres' host='localhost'"
    SECRET_KEY = 'KjkhFDjihkgy#$&(hdsdsddR#$gdd!'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    CONNECTION_STRING = 'postgres://lgltqihiazvjfw:10428ba23af1a311d539ab7a0f99f00c1efa2bbb34841b8bfad5d47d73df90e9@ec2-75-101-153-56.compute-1.amazonaws.com:5432/d3ruee63uidar1'

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production': ProductionConfig
}