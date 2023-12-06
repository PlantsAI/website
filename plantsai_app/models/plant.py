from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from plantsai_app import db


class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    water = db.Column(db.Text)

    def __init__(self, name, water):
        self.name = name
        self.water = water


class AddForm(FlaskForm):
    name = StringField('Name of Plant: ', validators=[DataRequired()])
    water = StringField('Watering Schedule: ', validators=[DataRequired()])
    submit = SubmitField('Add Plant')


class DelForm(FlaskForm):
    id = StringField('Id Number of Plant to Remove: ', validators=[DataRequired()])
    submit = SubmitField('Remove Plant')
