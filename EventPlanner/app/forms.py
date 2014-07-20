
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, DateTimeField, IntegerField, validators
from wtforms.validators import Required, Email
from wtforms.validators import ValidationError
#from models import User

class EventForm(Form):
    name = TextField('name', [Required('Name is required')])
    category = TextField('category', [Required('Category is required')])
    step = TextField('step', [Required('Step is required')])
    time = TextField('time', [Required('Time is required')])
    location = TextField('location', [Required('Location is required')])
    
