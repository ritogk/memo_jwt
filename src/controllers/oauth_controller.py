from os import access
from flask import request, redirect, jsonify, url_for, make_response
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
import jwt
from service.UserService import UserService
user_service = UserService()

from service.TwitterAuthService import TwitterAuthService
twitter_auth_service = TwitterAuthService()

from service.GoogleAuthService import GoogleAuthService
google_auth_service = GoogleAuthService()

import random
class OAuthController:
    def oauth_twitter_url(self):
        # twitterの認証画面のurlを取得
        return twitter_auth_service.get_authorization_url()
    
    def create_twitter_user(self):
        code = request.args.get("code")
        # codeからアクセストークンを取得
        access_token, refresh_token = twitter_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # twitterからユーザー情報取得
        twitter_user = twitter_auth_service.get_user_info(access_token)
        # ユーザー登録
        user = user_service.create_oauth_user('twitter', twitter_user['data']['name'], twitter_user['data']['id'] + '@' + str(random.random()), access_token, refresh_token)
        # jwt生成
        key = "secret"
        content = {}
        content["id"] = user.id
        token = jwt.encode(content, key, algorithm="HS256").decode('utf-8')
        server_domain = 'server.test.com'
        
        response = make_response({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
        response.headers.set('Content-Type', 'application/json')
        response.headers.add('X-Content-Type-Options', 'nosniff')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        
        response.set_cookie("token", value=token,
                        httponly=True, samesite=None,
                        domain=server_domain, path='/')
    
    def oauth_google_url(self):
        return google_auth_service.get_authorization_url()
    
    def create_google_user(self):
        code = request.args.get("code")
        # codeからアクセストークンを取得
        access_token, refresh_token = google_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # googleからユーザー情報取得
        google_user = google_auth_service.get_user_info(access_token)
        print(google_user)
        # ユーザー登録
        user = user_service.create_oauth_user('google', google_user['name'], google_user['email'], access_token, refresh_token)
        # jwt生成
        key = "secret"
        content = {}
        content["id"] = user.id
        token = jwt.encode(content, key, algorithm="HS256").decode('utf-8')
        server_domain = 'server.test.com'
        
        response = make_response({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
        response.headers.set('Content-Type', 'application/json')
        response.headers.add('X-Content-Type-Options', 'nosniff')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        
        response.set_cookie("token", value=token,
                        httponly=True, samesite=None,
                        domain=server_domain, path='/')
        return response
        
        
        
        