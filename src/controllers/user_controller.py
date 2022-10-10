from flask import request, redirect, url_for
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
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
        
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        

    # ログアウト
    def get_logout(self):
        pass
        # authenticate_service.logout()
        # return redirect(url_for('routes.get_index'))