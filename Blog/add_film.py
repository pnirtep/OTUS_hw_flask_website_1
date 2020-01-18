from flask import Blueprint, render_template, request, jsonify


add_film_app = Blueprint('add_film_app', __name__)


@add_film_app.route('/', endpoint='add-film')
def page_view():
    return render_template('add_film.html')

@add_film_app.route('/', methods=['POST'], endpoint='/form-add-film')
def form_data():
    r = request.form
    data = jsonify(r)
    return data

