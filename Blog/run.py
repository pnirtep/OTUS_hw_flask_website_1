from flask import Flask, render_template, redirect, request
from sqlalchemy.orm import sessionmaker
from Blog.blueprints.add_film import add_film_app
from Blog.blueprints.films import film_app
from Blog.blueprints.registration import registration_app
from Blog.models import Base, engine, User, Post
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # the login view of your application

app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"  # a secret key for your app
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(add_film_app, url_prefix='/add-film')
app.register_blueprint(film_app, url_prefix='/films')
app.register_blueprint(registration_app, url_prefix='/registration')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()

@app.route('/')
def home():
    auth_user = current_user.is_authenticated
    posts = session.query(Post).order_by(Post.id.desc())
    return render_template('index.html', auth_user=auth_user, posts=posts)


@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login_post():
    data = request.form
    login = data.get('login')
    password = data.get('password')
    user = session.query(User).filter_by(login=login, password=password).first()
    if user:
        login_user(user)
        return redirect('/')
    return redirect('/login')



@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'GET':
        auth_user = current_user.is_authenticated
        return render_template('logout.html', auth_user = auth_user)
    elif request.method == 'POST':
        logout_user()
        return redirect('/')




if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
