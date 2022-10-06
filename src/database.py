"""FlaskアプリがSQLAlchemyとFlask-Migrateを使えるようにするための初期化"""
from flask_sqlalchemy import SQLAlchemy

# from flask_sample.database import init_db

from flask_migrate import Migrate  # 追加

db = SQLAlchemy()