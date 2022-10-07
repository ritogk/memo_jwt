"""FlaskアプリがSQLAlchemyとFlask-Migrateを使えるようにするための初期化"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # 追加

db = SQLAlchemy()

def init_db(app):
    # sqlalchemyとflaskの連携
    db.init_app(app)
    # flask-migrateの設定
    migrate = Migrate(app, db)  # 追加
    migrate.init_app(app, db)