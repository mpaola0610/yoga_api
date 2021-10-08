from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class clicker(FlaskForm):
    yesOrno = SelectField('random', choices = ['Yes',"No"], validate_choice= True)

    submit_button = SubmitField('Build Sequence')