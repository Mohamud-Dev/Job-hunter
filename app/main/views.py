from flask import render_template, redirect, url_for,abort,request
from . import main
# from ..models import Hiring
from .forms import HireForm
from ..requests import get_jobs, search_jobs

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
    title = f'search results for {query}'
    return render_template('jobs.html',title=title,jobs = searched_jobs)


@main.route('/hire/new/', methods = ['GET','POST'])


def new_hire():
    form = HireForm()
    if form.validate_on_submit():
        location = form.location.data
        language = form.language.data
       
        new_hire = Hiring(location=location, language=language)
        

        return redirect(url_for('main.index'))
    return render_template('hire.html',form=form)
