from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """docstring for RegistrationForm."""

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[
        DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """docstring for RegistrationForm."""

    email = StringField('Email', validators=[
        DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class IMDBForm(FlaskForm):
    """docstring for IMDBForm."""

    user_review = TextAreaField('User Review', validators=[
                                DataRequired()], render_kw={"rows": 3, "cols": 11})
    submit = SubmitField('Submit')
