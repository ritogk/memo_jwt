from flask import current_app
import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session
from db.models.all import User, UserAuthentication, UserOauth
from db.db import db
import hashlib

class UserService:
  def create_user(self, name: str, email: str, username: str, password: str) -> User:
      password_hash = hashlib.sha256((password + current_app.config['USER_PASSWORD_SALT']).encode()).hexdigest()
      if(db.session.query(db.exists().where(UserAuthentication.username == username).where(UserAuthentication.password == password_hash)).scalar()):
        return '存在してます。'
      else:
        user = User(name, email)
        db.session.add(user)
        db.session.flush()
        user_authentication = UserAuthentication(name, email)
        user_authentication.user_id = user.id
        user_authentication.username = username
        user_authentication.password = password_hash
        db.session.add(user_authentication)
        db.session.commit()
        return user
      
  def login(self, username: str, password: str) -> User:
      password_hash = hashlib.sha256((password + current_app.config['USER_PASSWORD_SALT']).encode()).hexdigest()
      user_authentication = db.session.query(UserAuthentication).filter_by(username = username,
                                                                            password = password_hash).first()
      if not user_authentication:
        return 'パスワード又はユーザー名が間違っています。'
      
      return user_authentication.user
           
  def create_oauth_user(self, provider: str, name: str, email: str, access_token:str, refresh_token: str) -> User:
      if(db.session.query(db.exists().where(UserOauth.access_token == access_token).where(UserOauth.refresh_token == refresh_token)).scalar()):
        return '存在してます。'
      else:
        user = User(name, email)
        db.session.add(user)
        db.session.flush()
        print(user.id)
        user_oauth = UserOauth(user.id, provider, access_token, refresh_token)
        db.session.add(user_oauth)
        db.session.commit()
        return user  