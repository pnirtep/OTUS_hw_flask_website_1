from flask import Blueprint, render_template, request
from werkzeug.utils import redirect

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from ..create_functions import session_add, create_user, create_post, create_tag


engine = create_engine('sqlite:///my_blog.db')
Base = declarative_base()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


registration_app = Blueprint('registration_app', __name__)



@registration_app.route('/', methods=['GET'], endpoint='registration')
def register():
    """
    Маошрут на страницу решистрации, где содержится форма, которую может заполнить НЕавторизованный пользователь

    """
    return render_template('registration.html')


@registration_app.route('/', methods=['POST'], endpoint='registration_post')
def register_post():
    """
    При заполнении формы, пользователь указывает имя, логин, пароль, почту, которые сохраняются в БД для последующей
    авторизации на сайте.
    Так же осуществляется дополнительная проверка - в случае, если логин уже естьв в системе, покажется ошибка

    """
    data = request.form
    username = data.get('username')
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    try:
        create_user(username, login, email, password)
    except BaseException as e:
        error = 'Такой login уже занят'
        return render_template('registration.html', error=error)
    return redirect('success-reg', code=302)



@registration_app.route('/success-reg', methods=['GET'], endpoint='success-reg')
def register_success():
    """
    Маошрут на страницу с успешной регистрацией

    """
    return render_template('success_reg.html')

