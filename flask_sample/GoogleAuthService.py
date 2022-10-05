import os
import requests
from typing import Optional
from requests_oauthlib import OAuth2Session

class GoogleAuthService:
  GOOGLE_CLIENT_ID = "690002281063-rakv20u6usg5tp7ubd2lp4n7c656b2q7.apps.googleusercontent.com"
  GOOGLE_CLIENT_SECRET = "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"
  REDIRECT_URI = "https://7c3b-2400-2200-3eb-e896-a949-dc1f-fcc6-3f90.jp.ngrok.io"
  OAUTH_URL = "https://accounts.google.com/o/oauth2/auth"
  TOKEN_URL = "https://oauth2.googleapis.com/token"
  USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
  SCOPES = ['openid','https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
  
  def get_authorization_url(self) -> str:
      # ここでGoogle認証画面に遷移するためのURLを取得する
      # OAuthにない任意のパラメータをもたせたい場合は、 state を使うとよい
      # ex)
      #   # name を渡したい場合
      #   exp = int(datetime.utcnow().timestamp()) + 30
      #   encoded = jwt.encode({"exp": exp, "name": "hoge"}, "secrets", algorithm="HS256")
      #   state = encoded.decode("utf-8")
      #   redirect_url, _ = self._client().authorization_url(self.OAUTH_URL, state=state)

      redirect_url, _ = self._client().authorization_url(self.OAUTH_URL)
      return redirect_url

  def fetch_token(self, code: str) -> str:
      # Googleからリダイレクトして来たときにURLに付与されている code を使って token を取得する
      token = self._client().fetch_token(
          self.TOKEN_URL,
          client_secret=self.GOOGLE_CLIENT_SECRET,
          code=code,
      )
      return token["access_token"]

  def get_user_info(self, access_token: str) -> Optional[dict]:
      # access_token を使って、ユーザ情報を取得する
      endpoint_url = f"{self.USER_INFO_URL}?access_token={access_token}"
      print(endpoint_url)
      response = requests.get(endpoint_url)
      print(response)
      
      if response.status_code == 200:
          return response.json()

      return None

  def _client(self) -> OAuth2Session:
      return OAuth2Session(
          self.GOOGLE_CLIENT_ID,
          scope=self.SCOPES,
          redirect_uri=self.REDIRECT_URI
      )  