'''
Created on Jul 2, 2014

@author: lan_xu, alvin_yau
'''
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, DateTimeField, IntegerField, validators
from wtforms.validators import Required, Email
from wtforms.validators import ValidationError
#from models import User

class EventForm(Form):
    name = TextField('name', [Required('Name is required')])
    
