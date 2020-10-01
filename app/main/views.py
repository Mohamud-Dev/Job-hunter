from flask import render_template, redirect, url_for,abort,request
from . import main
from ..models import Hiring, User
from .forms import HireForm, UpdateProfile, bio
from ..requests import get_jobs, search_jobs, upload
from flask_login import login_required, current_user
from .. import db, photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting floods news
  
  
    jobs=get_jobs('all')
    title = 'welcome to Job Hunter'
    
    
    search_jobs = request.args.get('keyword')

    if search_jobs:
        return redirect(url_for('main.search',query=search_jobs))
    else:
        return render_template('index.html',jobs=jobs,title=title)



@main.route('/search/<query>')

def search(query):
    '''
    View function to display the search results
    '''
    
    
    query_list = query.split(" ")
    query_format = "+".join(query_list)
    searched_jobs = search_jobs(query_format)
    print(searched_jobs)
    title = f'search results for {query}'
    return render_template('jobs.html',title=title,jobs = searched_jobs)


@main.route('/hire/new/', methods = ['GET','POST'])
@login_required

def new_hire():
    form = HireForm()
    if form.validate_on_submit():
        location = form.location.data
        language = form.language.data
       
        new_hire = Hiring(location=location, language=language)
        

        return redirect(url_for('main.index'))
    return render_template('hire.html',form=form)

@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/user/update/bio/<uname>', methods= ['GET', 'POST'])
@login_required
def updatebio(uname):
    user = User.query.filter_by(username = uname).first()
    form =bio()
    if form.validate_on_submit():
        User.bio = form.bio.data
        
        db.session.commit()

        return redirect(url_for('main.profile', uname = user.username))

    return render_template ('profile/bio.html', form =form, user = user)
    