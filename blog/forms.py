from flask_wtf import FlaskForm 
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])


class Comment(FlaskForm):
    guest =  StringField("Логин", validators=[DataRequired()])
    text = TextAreaField("Пароль", validators=[DataRequired()])