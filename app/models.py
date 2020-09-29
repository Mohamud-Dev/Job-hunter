from flask import Flask
from . import db
from flask_login import UserMixin
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save_user(self):
        db.session.add(self)
        db.session.commit()



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


