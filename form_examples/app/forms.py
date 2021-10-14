from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired, NumberRange

class AddBookForm(FlaskForm):
    ''' Form for adding a new book '''
    title = StringField('Title:', validators=[InputRequired()])
    author = StringField('Author:', validators=[InputRequired()])
    rating = IntegerField('Rating:', validators=[InputRequired(), NumberRange(min=1, max=5)])
    genre_id = SelectField('Genre:', validators=[InputRequired()])
    submit = SubmitField('Add book')

class EditBookForm(AddBookForm):
    ''' Form for editing an existing book '''
    submit = SubmitField('Save changes')

class AddGenreForm(FlaskForm):
    ''' Form for adding a new genre '''
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add genre')

class EditGenreForm(AddGenreForm):
    ''' Form for editing an existing genre '''
    submit = SubmitField('Save changes')
