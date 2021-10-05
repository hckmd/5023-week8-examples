from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

class AddBookForm(FlaskForm):
    title = StringField('Title:', validators=[InputRequired()])
    author = StringField('Author:', validators=[InputRequired()])
    genre_id = SelectField('Genre:', validators=[InputRequired()])
    submit = SubmitField('Add book')

class EditBookForm(AddBookForm):
    submit = SubmitField('Save changes')

class AddGenreForm(FlaskForm):
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add genre')

class EditGenreForm(AddGenreForm):
    submit = SubmitField('Save changes')
