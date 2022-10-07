from flask import Flask
from routes import routes
import db.models.all
import db.db as db

# webアプリケーション作成
def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)
    # db関係の設定
    db.init_db(app)
    db.init_seeder(app)
    # ルーティングの設定
    app.register_blueprint(routes)
    return app

app = create_app()