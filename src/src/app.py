from flask import Flask, jsonify, render_template, make_response, request
from config.DevelopmentConfig import DevelopmentConfig
from routes import routes
import db.models.all
import db.db as db

# webアプリケーション作成
def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)
    # 環境変数
    app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_ECHO'] = DevelopmentConfig.SQLALCHEMY_ECHO
    app.config['TEMPLATES_AUTO_RELOAD'] = DevelopmentConfig.TEMPLATES_AUTO_RELOAD
    # db関係の設定
    db.init_db(app)
    # ルーティング
    app.register_blueprint(routes)
    return app

app = create_app()

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1100, debug=DevelopmentConfig.DEBUG)