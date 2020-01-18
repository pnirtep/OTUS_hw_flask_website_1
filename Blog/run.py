from flask import Flask, render_template, request
from Blog.add_film import add_film_app
from Blog.films import film_app



app = Flask(__name__)
app.register_blueprint(add_film_app, url_prefix='/add-film')
app.register_blueprint(film_app, url_prefix='/films')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():

    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)