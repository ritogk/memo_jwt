from distutils.command.config import config
import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session
from requests.auth import AuthBase, HTTPBasicAuth
from typing import Tuple

from Config import Config


class TwitterAuthService:
    TWITTER_CLIENT_ID = ""
    TWITTER_CLIENT_SECRET = ""
    REDIRECT_URI = ""
    OAUTH_URL = "https://twitter.com/i/oauth2/authorize"
    TOKEN_URL = "https://api.twitter.com/2/oauth2/token"
    USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
    SCOPES = ['tweet.read', 'users.read', 'offline.access']
    CODE_CHALLENGE = "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM"
    CODE_CHALLENGE_METHOD = "S256"
    CODE_VERIFIER = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"

    def __init__(self) -> None:
        config = Config.getInstance()
        self.TWITTER_CLIENT_ID = config.TWITTER_CLIENT_ID
        self.TWITTER_CLIENT_SECRET = config.TWITTER_CLIENT_SECRET
        self.REDIRECT_URI = config.SERVER_BASE_URL + '/oauth/callback'

    def get_authorization_url(self) -> str:
        redirect_url, _ = self._client().authorization_url(
            self.OAUTH_URL,
            code_challenge=self.CODE_CHALLENGE,
            code_challenge_method=self.CODE_CHALLENGE_METHOD,
        )
        return redirect_url

    def fetch_token(self, code: str) -> Tuple[str, str]:
        # Googleからリダイレクトして来たときにURLに付与されている code を使って token を取得する
        auth = HTTPBasicAuth(self.TWITTER_CLIENT_ID,
                             self.TWITTER_CLIENT_SECRET)
        token = self._client().fetch_token(
            self.TOKEN_URL,
            client_secret=self.TWITTER_CLIENT_SECRET,
            code=code,
            auth=auth,
            client_id=self.TWITTER_CLIENT_ID,
            include_client_id=True,
            code_verifier=self.CODE_VERIFIER,
        )
        print(token)
        return token['access_token'], token['refresh_token']

    def get_user_info(self, access_token: str) -> Optional[dict]:
        # access_token を使って、ユーザ情報を取得する
        params = {"user.fields": "created_at,description"}
        headers = {
            "Authorization": "Bearer {}".format(access_token),
        }
        url = "https://api.twitter.com/2/users/me"
        response = requests.request("GET", url, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text)
            )

        return response.json()

    def _client(self) -> OAuth2Session:
        return OAuth2Session(
            self.TWITTER_CLIENT_ID,
            scope=self.SCOPES,
            redirect_uri=self.REDIRECT_URI
        )
