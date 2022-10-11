from service.JwtService import JwtService
from flask import request, current_app
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
        content = {}
        content["id"] = user.id
        token = JwtService.generate_jwt(content)
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
        content = {}
        content["id"] = user.id
        token = JwtService.generate_jwt(content)
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

    # 全ユーザー取得
    def get_users(self):
        users = user_service.get_users()
        dicts = [{'id': user.id, 'name': user.name, 'email': user.email}
                 for user in users]
        response = base_response.generate_response({'users': dicts})
        return response
