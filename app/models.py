
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask import Flask
from . import db
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))    

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password_secure = db.Column(db.String)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    profile_pic_path = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @property
    def password(self):
        raise AttributeError('You cannot read password')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    


   


class Hiring:
    '''
    Article class to define Movie Objects
    '''

    def __init__(self,id,location,language):
        self.id = id
        self.location=location
        self.language = language

class Jobs:
    '''
    Jobs class to define articles objects
    '''
    def __init__(self,id,time,title,company,company_logo,url,location,date,description):
        self.id = id
        self.time = time
        self.title = title
        self.company = company
        self.company_logo = company_logo
        self.url = url
        self.location = location
        self.date = date
        self.description = description
       
     

   

       
        
