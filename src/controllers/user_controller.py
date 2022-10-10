from os import access
from flask import request, redirect, jsonify, url_for, make_response
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
import jwt
from service.UserService import UserService
user_service = UserService()
import random

from service.TwitterAuthService import TwitterAuthService
twitter_auth_service = TwitterAuthService()

class UserController:
    # ユーザーの新規登録(password認証)
    def create(self):
        name = request.json["name"]
        email = request.json["email"]
        username = request.json["username"]
        password = request.json["password"]
        user = user_service.create_user(name, email, username, password)
        
        # jwt生成
        key = "secret"
        content = {}
        content["id"] = user.id
        token = jwt.encode(content, key, algorithm="HS256").decode('utf-8')
        # result = jwt.decode(encoded, key, algorithms="HS256")
        # print(result)
        
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
        
    # ユーザーの新規登録(oauth認証)
    def create_oauth(self):
        code = request.json["code"]
        # codeからアクセストークンを取得
        access_token, refresh_token = twitter_auth_service.fetch_token(code)
        # twitterからユーザー情報取得
        twitter_user = twitter_auth_service.get_user_info(access_token)
        # ユーザー登録
        user = user_service.create_oauth_user(twitter_user['data']['name'], twitter_user['data']['id'] + '@' + str(random.random()), access_token, refresh_token)
        response = make_response({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
        response.headers.set('Content-Type', 'application/json')
        response.headers.add('X-Content-Type-Options', 'nosniff')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
        
        
        
        