from flask import request, redirect, jsonify, url_for, make_response
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
import jwt
from service.UserService import UserService
user_service = UserService()

class UserController:
    # 新規登録
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
        

    # ログアウト
    def get_logout(self):
        pass
        # authenticate_service.logout()
        # return redirect(url_for('routes.get_index'))