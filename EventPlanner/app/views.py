'''
Created on Jul 2, 2014

@author: alvin_yau
'''
from app import app, lm, sqldb
from models import User, Event, Team, Member
from forms import EventForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from datetime import datetime, date, time, timedelta


@app.route('/', methods = ['GET', 'POST'])
def hello():
    return render_template("hello.html")

@app.route('/createEvent', methods = ['GET', 'POST'])
def createEvent():
    form = EventForm()
    if form.validate_on_submit():
        flash('Event Created.')
    return render_template("createEvent.html", form=form)

@app.route('/suggestions/<string:type>', methods = ['GET', 'POST'])
def getSuggestions(type):
    return render_template("suggestions.html", data=type)


