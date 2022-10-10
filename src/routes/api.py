from flask import jsonify, render_template, make_response, request, Blueprint
from controllers.authentication_controller.authentication_controller import AuthenticationController

from controllers.user_controller import UserController
user_controller = UserController()

from service.TwitterAuthService import TwitterAuthService
twitter_auth_service = TwitterAuthService()

authentication_controller = AuthenticationController()

from controllers.oauth_controller import OAuthController
oauth_controller = OAuthController()

api = Blueprint("api", __name__)

# ユーザー登録
@api.route('/users', methods=['POST'])
def users():
    return user_controller.create()

# ログイン
@api.route('/users/login', methods=['POST'])
def users_login():
    return user_controller.login()

# ユーザー登録(oauth)
@api.route('/users/oauth/twitter', methods=['POST'])
def users_oauth():
    return oauth_controller.create_twitter_user()

# twitterの認証画面のurlを取得
@api.route('/oauth/twitter/url', methods=['GET'])
def oauth_twitter_url():
    return oauth_controller.oauth_twitter_url()

# twitterのoauth2認可後の処理
@api.route('/oauth/twitter/callback', methods=['GET'])
def oauth_redirect():
    return oauth_controller.create_twitter_user()

# googleの認証画面のurlを取得
@api.route('/oauth/google/url', methods=['GET'])
def oauth_google_url():
    return oauth_controller.oauth_google_url()

# googleのoauth2認可後の処理
@api.route('/oauth/google/callback', methods=['GET'])
def oauth_google_callback():
    return oauth_controller.create_google_user()

# 認証画面からリダイレクト時に返却されたcodeを使いaccess_tokenを取得する
@api.route('/twitter/fetch-token', methods=['GET'])
def twitter_fetch_token():
    code = request.args.get('code')
    access_token = twitter_auth_service.fetch_token(code)
    response = make_response(jsonify({'token': access_token}))    
    return response
    # return 

# アクセストークンを使ってユーザー情報を取得する
@api.route('/twitter/get-user-info', methods=['GET'])
def twitter_get_user_info():
    token = request.args.get('token')
    print('st')
    print(token)
    user_info = twitter_auth_service.get_user_info(token)
    print(user_info)
    response = make_response(user_info)
    return response

from service.GoogleAuthService import GoogleAuthService
google_auth_service = GoogleAuthService()
import base64
from urllib.parse import unquote
# 認証画面を表示するためのURLを取得する 
@api.route('/google/authorization-url', methods=['GET'])
def authorization_url():
    return google_auth_service.get_authorization_url()

# 認証画面からリダイレクト時に返却されたcodeを使いaccess_tokenを取得する
@api.route('/google/fetch-token', methods=['GET'])
def fetch_token():
    code = request.args.get('code')
    ## code = unquote(request.args.get('code').encode('utf-8'))
    ## return code
    access_token = google_auth_service.fetch_token(code)
    response = make_response(jsonify({'token': access_token}))    
    return response
    # return 

# アクセストークンを使ってユーザー情報を取得する
@api.route('/google/get-user-info', methods=['GET'])
def get_user_info():
    token = request.args.get('token')
    # return token
    print('st')
    print(token)
    user_info = google_auth_service.get_user_info(token)
    print(user_info)
    response = make_response(user_info)
    return response