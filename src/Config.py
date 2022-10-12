import os


class Config():
    __instance = None
    DEBUG = True
    DATABASE_FILE = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), './db/test.db')
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TEMPLATES_AUTO_RELOAD = True
    SERVER_BASE_URL = ''
    SERVER_DOMAIN = ''
    USER_PASSWORD_SALT = ''
    JWT_SECRET = ''

    TWITTER_CLIENT_ID = ""
    TWITTER_CLIENT_SECRET = ""

    GOOGLE_CLIENT_ID = ""
    GOOGLE_CLIENT_SECRET = ""

    @staticmethod
    def getInstance():
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance != None:
            raise Exception("Singletonクラス")
        else:
            Config.__instance = self
            # 環境変数読み込み
            self.DATABASE_FILE = os.getenv('DATABASE_FILE')
            self.SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
            self.SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
                'SQLALCHEMY_TRACK_MODIFICATIONS')
            self.SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')
            self.TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD')
            self.SERVER_BASE_URL = os.getenv('SERVER_BASE_URL')
            self.SERVER_DOMAIN = os.getenv('SERVER_DOMAIN')
            self.USER_PASSWORD_SALT = os.getenv('USER_PASSWORD_SALT')
            self.JWT_SECRET = os.getenv('JWT_SECRET')
            self.TWITTER_CLIENT_ID = os.getenv('TWITTER_CLIENT_ID')
            self.TWITTER_CLIENT_SECRET = os.getenv('TWITTER_CLIENT_SECRET')
            self.GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
            self.GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
