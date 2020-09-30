from flask import redirect, render_template, url_for,render_template, flash
from .forms import SignIn, SignUp
from ..models import User
from flask_login import login_user,logout_user
from . import auth
from .. import db
from flask_login import login_required


@auth.route('/profile/signup', methods = ['GET','POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username = username, email = email, password = password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.signin'))
    return render_template('authentification/register.html', form = form)
    
@auth.route('/profile/signin', methods = ['GET','POST'])
def signin():
    
    form = SignIn()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        

        if user is not None and user.password == form.password.data: 

            login_user(user,form.Remember.data)

            #return redirect(url_for('blogs.postedblogs'))

        flash('Invalid username or password')

    
    return render_template('authentification/SignIn.html', form = form)

@auth.route('/profile/signout', methods = ['GET','POST'])
@login_required
def signout():

    logout_user()

    return redirect(url_for('auth.signin'))



