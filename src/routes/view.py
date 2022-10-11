from flask import Blueprint, render_template

view = Blueprint("view", __name__)

# 画面


@view.route('/', methods=['GET'])
def hello():
    return render_template('hello.html')


@view.route('/oauth/callback', methods=['GET'])
def oauth_callback():
    return render_template('oauth_callback.html')
