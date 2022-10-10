from flask import Flask
from routes.api import api
from routes.view import view
import db.models.all
import db.db as db
from config.DevelopmentConfig import DevelopmentConfig

# webアプリケーション作成
def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)
    # db関係の設定
    db.init_db(app)
    db.init_seeder(app)
    # ルーティングの設定
    app.register_blueprint(view)
    app.register_blueprint(api)
    # その他
    app.config['JWT_SECRET'] = DevelopmentConfig.JWT_SECRET
    app.config['USER_PASSWORD_SALT'] = DevelopmentConfig.USER_PASSWORD_SALT
    return app

app = create_app()