from flask import Blueprint, render_template
from flask_login import current_user
from sqlalchemy.orm import sessionmaker

from Blog.models import Post, Base, engine

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

film_app = Blueprint('film_app', __name__)

@film_app.route('/', endpoint='films')
def page_view():
    auth_user = current_user.is_authenticated
    posts = session.query(Post).order_by(Post.id.desc())
    return render_template('film_page.html', auth_user = auth_user, posts=posts)

@film_app.route('/<int:post_id>', endpoint='film_view')
def film_view(post_id):
    auth_user = current_user.is_authenticated
    post = session.query(Post).filter_by(id=post_id).first()
    return render_template('film-template.html', auth_user = auth_user, post_id=id, post=post)
