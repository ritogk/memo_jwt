from flask import current_app
import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session
from db.models.all import User, UserAuthentication, UserOauth
from db.db import db
import hashlib
from typing import Union
from flask import current_app
import jwt


class JwtService:
    @classmethod
    def generate_jwt(self, content: dict) -> str:
        secret = current_app.config['JWT_SECRET']
        return jwt.encode(content, secret, algorithm="HS256").decode('utf-8')
