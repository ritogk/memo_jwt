from routes.middleware.ValidityJwt import validate_jwt
from controllers.oauth_controller import OAuthController
from flask import Blueprint
from controllers.user_controller import UserController
user_controller = UserController()
oauth_controller = OAuthController()
api = Blueprint("api", __name__)


@api.route('/users', methods=['POST'])
# ユーザー登録(password)
def users():
    return user_controller.create()


@api.route('/users/logout', methods=['POST'])
# ログアウト
def users_logout():
    return user_controller.logout()


@api.route('/users/login', methods=['POST'])
# ログイン(password)
def users_login():
    return user_controller.login()


@api.route('/users/oauth/twitter', methods=['POST'])
# ユーザー登録(twitter)
def users_oauth_twitter():
    return oauth_controller.create_twitter_user()


@api.route('/users/oauth/twitter/login', methods=['POST'])
# ログイン(twitter)
def users_oauth_twitter_login():
    return oauth_controller.users_oauth_twitter_login()


@api.route('/users/oauth/google', methods=['POST'])
# ユーザー新規登録(google)
def users_oauth_google():
    return oauth_controller.create_google_user()


@api.route('/users/oauth/google/login', methods=['POST'])
# ユーザーログイン(google)
def users_oauth_google_login():
    return oauth_controller.users_oauth_google_login()


@api.route('/oauth/google/url', methods=['GET'])
# ユーザー登録(google)
def oauth_google_url():
    return oauth_controller.oauth_google_url()


@api.route('/oauth/twitter/url', methods=['GET'])
# twitterの認証画面のurlを取得
def oauth_twitter_url():
    return oauth_controller.oauth_twitter_url()


@api.route('/users', methods=['GET'])
@validate_jwt
# 全ユーザーを取得
def get_users():
    return user_controller.get_users()
