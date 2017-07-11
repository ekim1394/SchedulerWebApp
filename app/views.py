from flask import render_template, flash, redirect
from app import app
from .forms import SchedulerForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Eugene'}  # fake user

    return render_template("index.html",
                           user=user,
                           title="Home")


@app.route('/about')
def about():
    return render_template("about.html",
                           title="About")


@app.route('/contact')
def contact():
    return render_template("contact.html",
                           title="Contact")


@app.route('/scheduler', methods=['GET', 'POST'])
def login():
    form = SchedulerForm()
    if form.validate_on_submit():
        flash('Scheduled for %s' % form.date.data)
        return redirect('/index')
    return render_template('scheduler.html',
                           title='Schedule a date!',
                           form=form)
