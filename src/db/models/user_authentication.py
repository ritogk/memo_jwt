from datetime import datetime
from db.db import db

class UserAuthentication(db.Model):

    __tablename__ = 'users_authentications'

    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    username = db.Column(db.String(16), index=True, unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    def __init__(self, id, username, password, created_at=None, updated_at=None):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at