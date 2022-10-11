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
    SERVER_BASE_URL = 'https://fbb7-2400-2651-47e0-e000-c05-5b9-f27e-3446.jp.ngrok.io'
    USER_PASSWORD_SALT = 'flask_app_user_salt'
    JWT_SECRET = 'secret_key_test'

Config = DevelopmentConfig