import random
from os import access
from flask import request, redirect, jsonify, url_for, make_response, current_app
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
import jwt
from datetime import datetime
from service.response.response_authentication_token import response_authentication_token
from service.response.base_response import base_response
from service.UserService import UserService
user_service = UserService()


class UserController:
    # ユーザーの新規登録(password認証)
    def create(self):
        name = request.json["name"]
        email = request.json["email"]
        username = request.json["username"]
        password = request.json["password"]
        user = user_service.create_user(name, email, username, password)

        # jwt生成
        key = current_app.config['JWT_SECRET']
        content = {}
        content["id"] = user.id
        token = jwt.encode(content, key, algorithm="HS256").decode('utf-8')
        body = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        response = response_authentication_token.generate_response(body, token)
        return response

    # ログイン
    def login(self):
        username = request.json['username']
        password = request.json['password']
        user = user_service.login(username, password)

        # jwt生成
        key = current_app.config['JWT_SECRET']
        content = {}
        content["id"] = user.id
        token = jwt.encode(content, key, algorithm="HS256").decode('utf-8')
        data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        response = response_authentication_token.generate_response(data, token)
        return response

    # ログアウト
    def logout(self):
        response = base_response.generate_response({
            'success': True})
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.delete_cookie(
            "token", domain=current_app.config['SERVER_DOMAIN'])
        return response
