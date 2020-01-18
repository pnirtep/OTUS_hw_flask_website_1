from flask import Blueprint, render_template
from Blog.films_db import knifes_out as ko

film_app = Blueprint('film_app', __name__)





@film_app.route('/home-alone', endpoint='home-alone')
def page_view():
    return render_template('home-alone.html')

@film_app.route('/knifes-out', endpoint='knifes-out')
def page_view():
    r = ko
    return render_template('knifes-out.html', **r)
