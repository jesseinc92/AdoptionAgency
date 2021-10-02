from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    '''Creates a form to add a pet to the adoption listing.'''
    
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30.')])
    notes = StringField('Notes', validators=[Optional()])
    
    
class DispEditPetForm(FlaskForm):
    '''Creates display/edit pet form.'''
    
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available')