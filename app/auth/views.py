
from flask import redirect, render_template, url_for,render_template, flash,request
from .forms import SignIn, SignUp, LoginForm
from ..models import User
from . import auth
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm




@auth.route('/auth/register', methods = ['GET','POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username = username, email = email, password = password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('authentification.SignIn'))
    return render_template('auth/register.html', form = form)
    
@auth.route('/authentification/SignIn', methods = ['GET','POST'])
def signin():
    
    form = SignIn()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        

        if user is not None and user.password == form.password.data: 

            login_user(user,form.Remember.data)

            #return redirect(url_for('blogs.postedblogs'))

        flash('Invalid username or password')

    
    return render_template('authentification/SignIn.html', form = form)





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
    
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitcher login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('main.index'))
