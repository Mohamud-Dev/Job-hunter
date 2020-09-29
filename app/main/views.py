from flask import render_template, redirect, url_for,abort,request
from . import main
from ..models import Hiring

@main.route('/')
def index():
    title="Welcome to Job hunter!"
    

    return render_template('index.html', title=title)


@main.route('/hire/new/', methods = ['GET','POST'])


def new_hire():
    form = Hire()
    if form.validate_on_submit():
        location = form.location.data
        language = form.language.data
       
        new_hire = Hiring(location=location, language=language)
        new_hire.save_hire()

        return redirect(url_for('main.index'))
    return render_template('hire.html',form=form)
