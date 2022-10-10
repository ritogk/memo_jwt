from datetime import datetime
from db.db import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True, default='')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    user_authentications = db.relationship("UserAuthentication", backref="users")
    user_oauths = db.relationship("UserOauth", backref="users")
    
    def __init__(self, name, email, created_at=None, updated_at=None):
        self.name = name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at