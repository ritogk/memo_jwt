import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session
from db.models.all import User, UserAuthentication
from db.db import db
import hashlib

class UserService:
  def create_user(self, name: str, email: str, username: str, password: str) -> User:
      password_hash = hashlib.sha256(password.encode()).hexdigest()
      if(db.session.query(db.exists().where(UserAuthentication.username == username).where(UserAuthentication.password == password_hash)).scalar()):
        return '存在してます。'
      else:
        user = User(name, email)
        db.session.add(user)
        user_authentication = UserAuthentication(name, email)
        user_authentication.users_id = user.id
        user_authentication.username = username
        user_authentication.password = password_hash
        db.session.add(user_authentication)
        db.session.commit()
        return user
      