from flask import Blueprint, render_template
from flask_login import current_user



film_app = Blueprint('film_app', __name__)



@film_app.route('/home-alone', endpoint='home-alone')
def page_view():
    auth_user = current_user.is_authenticated
    return render_template('home-alone.html', auth_user = auth_user)

@film_app.route('/knifes-out', endpoint='knifes-out')
def page_view():
    pass
