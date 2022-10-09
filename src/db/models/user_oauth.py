from datetime import datetime
from db.db import db

class UserOauth(db.Model):

    __tablename__ = 'users_oauths'

    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    access_token = db.Column(db.String(1000))
    refresh_token = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    def __init__(self, id, access_token, refresh_token, created_at=None, updated_at=None):
        self.id = id
        self.username = access_token
        self.password = refresh_token
        self.created_at = created_at
        self.updated_at = updated_at