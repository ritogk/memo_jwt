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

class OAuthController:
    def oauth_twitter_url(self):
        # twitterの認証画面のurlを取得
        return twitter_auth_service.get_authorization_url()
        
        
        
        