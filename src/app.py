from flask import Flask, jsonify, render_template, make_response, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from config.DevelopmentConfig import DevelopmentConfig
# from models.models import User
from routes import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = DevelopmentConfig.SQLALCHEMY_ECHO
app.config['TEMPLATES_AUTO_RELOAD'] = DevelopmentConfig.TEMPLATES_AUTO_RELOAD

# ルーティング
app.register_blueprint(routes)

db = SQLAlchemy(app)
# flaskとsqlalchemyの連携を行う。
db.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)

from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
## おまじない
if __name__ == "__main__":
    # with app.app_context():
    #     # テーブル作成
    #     # db.create_all()
    app.run(host='0.0.0.0', port=1100, debug=DevelopmentConfig.DEBUG)