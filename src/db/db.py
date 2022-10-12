"""FlaskアプリがSQLAlchemyとFlask-Migrateを使えるようにするための初期化"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

from Config import Config
import os
db = SQLAlchemy()
seeder = FlaskSeeder()

# dbの初期設定を行います。


def init_db(app):
    config = Config.getInstance()
    # sqlliteの設定
    db_path = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), config.DATABASE_FILE)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_ECHO'] = config.SQLALCHEMY_ECHO
    app.config['TEMPLATES_AUTO_RELOAD'] = config.TEMPLATES_AUTO_RELOAD
    # sqlalchemyとflaskの連携
    db.init_app(app)
    # flask-migrateの設定
    migrate = Migrate(app, db)  # 追加
    migrate.init_app(app, db)


def init_seeder(app):
    seeder.init_app(app, db)
