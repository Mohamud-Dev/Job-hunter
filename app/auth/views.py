from flask import render_template,url_for,flash,redirect
from . import auth
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm
from app import db
from ..models import User

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data, bio = form.bio.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        
        return redirect(url_for('main.index', user = new_user))
    
    return render_template('auth/register.html', form = form)
    
    
