import os


class DevelopmentConfig:
    # Flask
    DEBUG = True
    databese_file = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), '../db/test.db')
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + databese_file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TEMPLATES_AUTO_RELOAD = True
    SERVER_BASE_URL = 'https://df6e-2400-2200-622-b4b8-41f2-2585-d918-4047.jp.ngrok.io'
    SERVER_DOMAIN = 'df6e-2400-2200-622-b4b8-41f2-2585-d918-4047.jp.ngrok.io'
    USER_PASSWORD_SALT = 'flask_app_user_salt'
    JWT_SECRET = 'secret_key_test'


Config = DevelopmentConfig
