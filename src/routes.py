from flask import jsonify, render_template, make_response, request, Blueprint
from service.TwitterAuthService import TwitterAuthService
twitter_auth_service = TwitterAuthService()

routes = Blueprint("routes", __name__)

# 認証画面を表示するためのURLを取得する 
@routes.route('/twitter/authorization-url')
def twitter_authorization_url():
    return twitter_auth_service.get_authorization_url()

# 認証画面からリダイレクト時に返却されたcodeを使いaccess_tokenを取得する
@routes.route('/twitter/fetch-token')
def twitter_fetch_token():
    code = request.args.get('code')
    access_token = twitter_auth_service.fetch_token(code)
    response = make_response(jsonify({'token': access_token}))    
    return response
    # return 

# アクセストークンを使ってユーザー情報を取得する
@routes.route('/twitter/get-user-info')
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
@routes.route('/google/authorization-url')
def authorization_url():
    return google_auth_service.get_authorization_url()

# 認証画面からリダイレクト時に返却されたcodeを使いaccess_tokenを取得する
@routes.route('/google/fetch-token')
def fetch_token():
    code = request.args.get('code')
    ## code = unquote(request.args.get('code').encode('utf-8'))
    ## return code
    access_token = google_auth_service.fetch_token(code)
    response = make_response(jsonify({'token': access_token}))    
    return response
    # return 

# アクセストークンを使ってユーザー情報を取得する
@routes.route('/google/get-user-info')
def get_user_info():
    token = request.args.get('token')
    # return token
    print('st')
    print(token)
    user_info = google_auth_service.get_user_info(token)
    print(user_info)
    response = make_response(user_info)
    return response

## 画面
@routes.route('/')
def hello():
    return render_template('hello.html')