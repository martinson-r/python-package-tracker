from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from map.map import map


class ShippingForm(FlaskForm):
  sender = StringField('Sender', validators=[DataRequired()])
  recipient = StringField('Recipient', validators=[DataRequired()])
  origin = SelectField('Origin', choices=[ (city, city) for city in map.keys()])
  destination = SelectField('Destination', choices=[ (city, city) for city in map.keys()])
  express_shipping = BooleanField('Express Shipping?')
  submit = SubmitField('Submit')
  cancel = SubmitField('Cancel')

