from calendar import c
from flask import current_app
import random
from service.GoogleAuthService import GoogleAuthService
from service.TwitterAuthService import TwitterAuthService
from flask import request, redirect, jsonify, url_for, make_response, current_app
from service.response.response_authentication_token import response_authentication_token
from service.response.base_response import base_response
from service.JwtService import JwtService
from service.UserService import UserService
user_service = UserService()

twitter_auth_service = TwitterAuthService()
google_auth_service = GoogleAuthService()


class OAuthController:
    # twitterの認証画面URLを取得します。

    def oauth_twitter_url(self):
        # twitterの認証画面のurlを取得
        url = twitter_auth_service.get_authorization_url()
        response = base_response.generate_response({
            'url': url
        })
        return response

    # twitter側で認可されたユーザーを登録します。
    def create_twitter_user(self):
        code = request.json["code"]
        # codeからアクセストークンを取得
        access_token, refresh_token = twitter_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # twitterからユーザー情報取得
        twitter_user = twitter_auth_service.get_user_info(access_token)

        # ユーザー登録
        user = user_service.create_oauth_user(
            'twitter', twitter_user['data']['name'], twitter_user['data']['id'] + '@' + str(random.random()), twitter_user['data']['id'])

        # jwt生成
        content = {}
        content["id"] = user.id
        content["name"] = user.name
        token = JwtService.generate_jwt(content)

        # respnse生成
        body = {
            'id': content["id"]
        }
        response = response_authentication_token.generate_response(body, token)

        return response

    # twitterのoauthを使ってログインを行います。
    def users_oauth_twitter_login(self):
        code = request.json["code"]
        # codeからアクセストークンを取得
        access_token, refresh_token = twitter_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # twitterからユーザー情報取得
        twitter_user = twitter_auth_service.get_user_info(access_token)

        oauth_user = user_service.get_oauth_user(
            'twitter', twitter_user['data']['id'])
        if (oauth_user == None):
            return 'errorです。'
        # jwt生成
        content = {}
        content["id"] = oauth_user.id
        content["name"] = oauth_user.name
        token = JwtService.generate_jwt(content)

        # response生成
        body = {
            'id': content["id"]
        }
        response = response_authentication_token.generate_response(body, token)

        return response

    # googleの認証画面URLを取得します。
    def oauth_google_url(self):
        url = google_auth_service.get_authorization_url()
        response = base_response.generate_response({
            'url': url
        })
        return response

    # googleに認可されたユーザーを登録します。
    def create_google_user(self):
        code = request.json["code"]
        # codeからアクセストークンを取得
        access_token, refresh_token = google_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # googleからユーザー情報取得
        google_user = google_auth_service.get_user_info(access_token)
        print(google_user)

        # ユーザー登録
        user = user_service.create_oauth_user(
            'google', google_user['name'], google_user['email'], google_user['id'])

        # jwt生成
        content = {}
        content["id"] = google_user['id']
        token = JwtService.generate_jwt(content)

        # response生成
        body = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        response = response_authentication_token.generate_response(body, token)

        return response

    # googleのoauthを使ってログインを行います。
    def users_oauth_google_login(self):
        code = request.json["code"]
        # codeからアクセストークンを取得
        access_token, refresh_token = google_auth_service.fetch_token(code)
        print(access_token)
        print(refresh_token)
        # googleからユーザー情報取得
        google_user = google_auth_service.get_user_info(access_token)
        print(google_user)

        oauth_user = user_service.get_oauth_user('google', google_user['id'])

        # jwt生成
        content = {}
        content["id"] = oauth_user.id
        token = JwtService.generate_jwt(content)

        # response生成
        body = {
            'id': content["id"]
        }
        response = response_authentication_token.generate_response(body, token)

        return response
