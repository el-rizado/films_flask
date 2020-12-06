from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


@app.route('/')
def login():
    """ This is the main page of the file """
    render_template('login.html')


@app.route('/films')
def show_films():
    return 'films'


@app.route('/actors')
def show_actors():
    return 'actors'


@app.route('/films/<int:film_id>')
def film_info(film_id):
    return 'film information'


if "__name__" == "__main__":
    app.run("0.0.0.0", 5000)
