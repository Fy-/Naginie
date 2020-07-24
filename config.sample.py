import os 

root = os.path.dirname(__file__)

class Config(object):
    ### GLOBAL ###
    HOST = "0.0.0.0"
    PORT = 8888
    SECRET_KEY = "secretkeygglol"

    ### SQLALCHEMY ###
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://naginie:pwd@localhost/naginie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_POOL_TIMEOUT = 20

    ### Naginie Config ###
    THEMES_DIRECTORY = os.path.join(root, 'naginie_themes')


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
