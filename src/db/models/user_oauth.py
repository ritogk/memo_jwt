from datetime import datetime
from db.db import db

class UserOauth(db.Model):

    __tablename__ = 'user_oauths'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    provider = db.Column(db.String(200), nullable=False)
    access_token = db.Column(db.String(1000))
    refresh_token = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    def __init__(self, user_id, provider, access_token, refresh_token, created_at=None, updated_at=None):
        self.user_id = user_id
        self.provider = provider
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.created_at = created_at
        self.updated_at = updated_at