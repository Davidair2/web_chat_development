from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    userinfo = db.relationship('UserInfo', backref='user', lazy='dynamic')
    posts = db.relationship('Posts', backref='user', lazy='dynamic')

    
    def __repr__(self):
        return '<User {}>'.format(self.email)
    
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dob = db.Column(db.DateTime, index=True)
    country = db.Column(db.String(64))
    city = db.Column(db.String(64))
    
    def __repr__(self):
        return '<UserInfo {}>'.format(self.first_name)
    
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_message = db.Column(db.String(300))
    gpt_response = db.Column(db.String(300))
    datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)