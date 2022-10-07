"""FlaskアプリがSQLAlchemyとFlask-Migrateを使えるようにするための初期化"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from config.DevelopmentConfig import DevelopmentConfig

db = SQLAlchemy()
seeder = FlaskSeeder()

# dbの初期設定を行います。
def init_db(app):
    # sqlliteの設定
    app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_ECHO'] = DevelopmentConfig.SQLALCHEMY_ECHO
    app.config['TEMPLATES_AUTO_RELOAD'] = DevelopmentConfig.TEMPLATES_AUTO_RELOAD
    # sqlalchemyとflaskの連携
    db.init_app(app)
    # flask-migrateの設定
    migrate = Migrate(app, db)  # 追加
    migrate.init_app(app, db)
    
def init_seeder(app):
    seeder.init_app(app, db)