from environs import Env

env = Env()
env.read_env()

ENV = env.str("NAGINIE_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")

SQLALCHEMY_DATABASE_URI= env.str("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = env.str("SQLALCHEMY_TRACK_MODIFICATIONS")

