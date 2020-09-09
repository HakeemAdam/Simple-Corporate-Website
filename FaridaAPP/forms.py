from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, \
    BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError


class ContactForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired("Enter your first name")])
    lastName = StringField('Last Name', validators=[DataRequired("Enter your last name")])
    email = StringField('E-mail', validators=[DataRequired("Enter a valid email address")])
    subject = StringField('Subject', validators=[DataRequired("What's the nature of your message?")])
    message = TextAreaField('Message', validators=[DataRequired("Didn't you want to say something?")])
    submit = SubmitField('Send')
