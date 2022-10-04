from flask import Flask, jsonify, render_template, make_response, request
app = Flask(__name__)

from GoogleAuthService import GoogleAuthService
google_auth_service = GoogleAuthService()
import base64
from urllib.parse import unquote

@app.route('/authorization-url')
def authorization_url():
    return google_auth_service.get_authorization_url()
    
@app.route('/fetch-token')
def fetch_token():
    code = request.args.get('code')
    ## code = unquote(request.args.get('code').encode('utf-8'))
    ## return code
    access_token = google_auth_service.fetch_token(code)
    response = make_response(jsonify({'token': access_token}))    
    return response
    # return 

@app.route('/get-user-info')
def get_user_info():
    token = request.args.get('token')
    # return token
    print('st')
    print(token)
    user_info = google_auth_service.get_user_info(token)
    print(user_info)
    response = make_response(user_info)
    return response

## 画面
@app.route('/')
def hello():
    return render_template('hello.html')

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1100, debug=True)


# clientId: 690002281063-rakv20u6usg5tp7ubd2lp4n7c656b2q7.apps.googleusercontent.com
# client secret: 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