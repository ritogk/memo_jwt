from flask import Flask, jsonify, render_template, make_response, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from config.DevelopmentConfig import DevelopmentConfig
from models.models import User
from routes.routes import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = DevelopmentConfig.SQLALCHEMY_ECHO
app.config['TEMPLATES_AUTO_RELOAD'] = DevelopmentConfig.TEMPLATES_AUTO_RELOAD
app.register_blueprint(routes)

# db = SQLAlchemy(app)
# # init_db(app)
# migrate = Migrate(app, db)

## おまじない
if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    #     db.session.commit()
    #     # print(man1, man2, man3)
    app.run(host='0.0.0.0', port=1100, debug=True)