'''
Created on Jul 2, 2014

@author: alvin_yau
'''
from app import app, lm, sqldb
#from models import User, Event, Team, Member
from models import Event, Suggestion, Step
from forms import EventForm, StepForm
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
        return event.id
    if form.validate_on_submit():
        eventId = add_event(form.name.data, form.category.data, form.step.data, form.time.data, form.location.data)
        #flash('Event Created.' + " Event ID: " + str(eventId))
        return redirect("addStep/"+str(eventId))

    return render_template("createEvent.html", form=form)

@app.route('/viewEvent/<int:id>', methods = ['GET'])
def viewEvent(id):
    event = Event.query.get(id)
    event_steps = Step.query.filter(Step.event_id==id)
    return render_template("viewEvent.html", event=event, event_steps=event_steps)

@app.route('/suggestions/<string:category>', methods = ['GET', 'POST'])
def getSuggestions(category):
    suggestions = Suggestion.query.filter(Suggestion.category == category)
    return render_template("suggestions.html", category=category, suggestions=suggestions)


@app.route('/addStep/<int:event_id>', methods = ['GET', 'POST'])
def addStep(event_id):
    event = Event.query.get(event_id)
    form = StepForm()
    def add_step(event_id, step_num, step):
        new_step = Step(event_id = event_id, step_num = step_num, step=step)
        sqldb.session.add(new_step)
        sqldb.session.commit()
    if form.validate_on_submit():
        add_step(event_id, form.step_num.data, form.step.data)
        return redirect("viewEvent/"+str(event_id))
    return render_template("addStep.html", form = form, event=event)