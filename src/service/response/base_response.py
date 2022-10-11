import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session
from typing import Tuple
from flask import request, redirect, jsonify, url_for, make_response, current_app, Response
from datetime import datetime
import jwt


class base_response:
    @classmethod
    def generate_response(self, body: dict) -> Response:
        response = make_response(body)
        response.headers.set('Content-Type', 'application/json')
        response.headers.add('X-Content-Type-Options', 'nosniff')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
