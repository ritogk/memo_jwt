import os


class DevelopmentConfig:
    # Flask
    DEBUG = True
    databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + databese_file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TEMPLATES_AUTO_RELOAD = True


Config = DevelopmentConfig