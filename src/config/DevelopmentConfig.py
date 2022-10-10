import os


class DevelopmentConfig:
    # Flask
    DEBUG = True
    databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../db/test.db')
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + databese_file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TEMPLATES_AUTO_RELOAD = True
    USER_PASSWORD_SALT = 'flask_app_user_salt'
    JWT_SECRET = 'secret_key_test'

Config = DevelopmentConfig