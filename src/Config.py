import os


class Config():
    __instance = None
    # db
    DATABASE_FILE = ''
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TEMPLATES_AUTO_RELOAD = True
    # server 情報
    SERVER_BASE_URL = ''
    SERVER_DOMAIN = ''
    # passwordのハッシュ化用のソルト
    USER_PASSWORD_SALT = ''
    # jwtの改ざんチェック用の鍵
    JWT_SECRET = ''
    # oauth2 twitter
    TWITTER_CLIENT_ID = ""
    TWITTER_CLIENT_SECRET = ""
    # oauth2 google
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
