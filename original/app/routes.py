from flask import render_template, redirect, url_for

from app import app, db
from app.models import Book, Genre
from app.forms import AddBookForm, AddGenreForm, EditBookForm, EditGenreForm

@app.route('/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', title = 'Books', books = books)

@app.route('/books/<int:id>')
def book_details(id):
    book = Book.query.get_or_404(id)
    return render_template('book_details.html', title = 'Book details', book = book)

@app.route('/books/add', methods = ['GET', 'POST'])
def book_add():
    form = AddBookForm()
    form.genre_id.choices = [(genre.id, genre.name) for genre in Genre.query.all()]
    if form.validate_on_submit():
        book = Book()
        form.populate_obj(obj=book)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('book_list'))
    return render_template('book_add.html', form = form, title = 'Add book')

@app.route('/books/<int:id>/edit', methods = ['GET', 'POST'])
def book_edit(id):
    book = Book.query.get_or_404(id)
    form = EditBookForm(obj=book)
    form.genre_id.choices = [(genre.id, genre.name) for genre in Genre.query.all()]
    if form.validate_on_submit():
        form.populate_obj(obj=book)
        db.session.commit()
        return redirect(url_for('book_details', id=book.id))
    return render_template('book_edit.html', title = 'Book edit', form = form, book = book)

@app.route('/books/<int:id>/delete')
def book_delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('book_list'))

@app.route('/genres')
def genre_list():
    genres = Genre.query.all()
    return render_template('genre_list.html', title = 'Genres', genres = genres)

@app.route('/genes/add', methods = ['GET', 'POST'])
def genre_add():
    form = AddGenreForm()
    if form.validate_on_submit():
        genre = Genre()
        form.populate_obj(obj=genre)
        db.session.add(genre)
        db.session.commit()
        return redirect(url_for('genre_list'))
    return render_template('genre_add.html', form = form, title = 'Add genre')

@app.route('/genres/<int:id>')
def genre_details(id):
    genre = Genre.query.get_or_404(id)
    return render_template('genre_details.html', title = 'Genre details', genre = genre)

@app.route('/genres/<int:id>/delete')
def genre_delete(id):
    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()
    return redirect(url_for('genre_list'))

@app.route('/genres/<int:id>/edit', methods = ['GET', 'POST'])
def genre_edit(id):
    genre = Genre.query.get_or_404(id)
    form = EditGenreForm(obj=genre)
    if form.validate_on_submit():
        form.populate_obj(obj=genre)
        db.session.commit()
        return redirect(url_for('genre_details', id = genre.id))
    return render_template('genre_edit.html', title = 'Edit genre', form = form, genre = genre)

