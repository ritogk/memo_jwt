from db.models.all import User, UserAuthentication, UserOauth
from db.db import db
import hashlib
from typing import Union
from typing import List

from Config import Config


class UserService:
    config = Config.getInstance()
    # ユーザー登録(password認証)

    def create_user(self, name: str, email: str, username: str, password: str) -> User:
        password_hash = hashlib.sha256(
            (password + self.config.USER_PASSWORD_SALT).encode()).hexdigest()
        if (db.session.query(db.exists().where(UserAuthentication.username == username).where(UserAuthentication.password == password_hash)).scalar()):
            return '存在してます。'
        else:
            user = User(name, email)
            db.session.add(user)
            db.session.flush()
            user_authentication = UserAuthentication(name, email)
            user_authentication.user_id = user.id
            user_authentication.username = username
            user_authentication.password = password_hash
            db.session.add(user_authentication)
            db.session.commit()
            return user

    # ログイン(password認証)
    def login(self, username: str, password: str) -> User:
        password_hash = hashlib.sha256(
            (password + self.config.USER_PASSWORD_SALT).encode()).hexdigest()
        user_authentication = db.session.query(UserAuthentication).filter_by(username=username,
                                                                             password=password_hash).first()
        if not user_authentication:
            return 'パスワード又はユーザー名が間違っています。'

        return user_authentication.user

    # ユーザー登録(oauth)
    def create_oauth_user(self, provider: str, name: str, email: str, identity: str) -> User:
        user = User(name, email)
        db.session.add(user)
        db.session.flush()
        print(user.id)
        user_oauth = UserOauth(user.id, provider, identity)
        db.session.add(user_oauth)
        db.session.commit()
        return user

    # ユーザー取得(oauth)
    def get_oauth_user(self, provider: str, identity: str) -> Union[User, None]:
        user_oauth: UserOauth = db.session.query(UserOauth).filter_by(
            identity=identity, provider=provider).first()

        print(user_oauth)
        if (user_oauth):
            return user_oauth.user
        else:
            return None

    # 全ユーザー取得
    def get_users(self) -> List[str]:
        users: List[User] = db.session.query(User).all()
        return users
