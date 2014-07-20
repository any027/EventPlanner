'''
Created on Jul 2, 2014

@author: alvin_yau
'''
from app import app, lm, sqldb
#from models import User, Event, Team, Member
from models import Event, Suggestion
from forms import EventForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from datetime import datetime, date, time, timedelta


@app.route('/', methods = ['GET', 'POST'])
def hello():
    events = Event.query.all()
    return render_template("hello.html", events=events)

@app.route('/createEvent', methods = ['GET', 'POST'])
def createEvent():
    form = EventForm()
    def add_event(name, category, steps, time, location):
        event = Event(name=name, category=category, steps=steps, time=time, location=location)
        sqldb.session.add(event)
        sqldb.session.commit()
    if form.validate_on_submit():
        add_event(form.name.data, form.category.data, form.step.data, form.time.data, form.location.data)
        flash('Event Created.')

    return render_template("createEvent.html", form=form)

@app.route('/viewEvent/<int:id>', methods = ['GET'])
def viewEvent(id):
    event = Event.query.get(id)
    return render_template("viewEvent.html", event=event)

@app.route('/suggestions/<string:category>', methods = ['GET', 'POST'])
def getSuggestions(category):
    suggestions = Suggestion.query.filter(Suggestion.category == category)
    return render_template("suggestions.html", category=category, suggestions=suggestions)


