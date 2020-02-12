from flask import Blueprint, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.utils import redirect



from ..create_functions import session_add, create_user, create_post, create_tag

engine = create_engine('sqlite:///my_blog.db')
Base = declarative_base()

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


registration_app = Blueprint('registration_app', __name__)



@registration_app.route('/', methods=['GET'], endpoint='registration')
def register():
    return render_template('registration.html')


@registration_app.route('/', methods=['POST'], endpoint='registration_post')
def register_post():
    data = request.form
    username = data.get('username')
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    create_user(username, login, email, password)
    return redirect('success-reg', code=302)



@registration_app.route('/success-reg', methods=['GET'], endpoint='success-reg')
def register():
    return render_template('success_reg.html')

