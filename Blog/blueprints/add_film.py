from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.utils import redirect

from ..create_functions import session_add, create_user, create_post, create_tag

engine = create_engine('sqlite:///my_blog.db')
Base = declarative_base()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


add_film_app = Blueprint('add_film_app', __name__)


@add_film_app.route('/', endpoint='add-film')
@login_required
def page_view():
    """
        В случае, если пользователь авторизован, ему доступна возможность заходить на страницу, с формой для добавления
        публикаций на сайте
    """
    auth_user = current_user.is_authenticated
    return render_template('add_film.html', auth_user=auth_user)

@add_film_app.route('/', methods=['POST'], endpoint='/form-add-film')
@login_required
def form_data():
    """
        В случае, если пользователь авторизован, он заполняет данные в форме о фильме и они передаются в БД, после чего
        происходит переадресация на страницу с фильмами

    """
    r = request.form
    film_title = r.get('film_title')
    film_text = r.get('film_text')
    create_post(film_title, film_text, current_user.username)
    return redirect('/')


