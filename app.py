from flask import Flask, render_template, request, make_response
import dbconnect

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
def login():
    """ This is the main page of the file """
    return render_template('login.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile_logged():
    if request.method == 'POST':
        username = request.form['uname']
        response = make_response(render_template('profile.html', username=username))
        response.set_cookie('userID', username)
        return response
    else:
        username = get_cookie()
        return render_template('profile.html', username=username)


def get_cookie():
    username = request.cookies.get('userID')
    return username


@app.route('/profile/films')
def show_films():
    username = get_cookie()
    conn = dbconnect.connect()
    try:
        with conn.cursor() as curs:
            curs.execute('SELECT film_id, title, release_year, description FROM film ORDER BY title;')
            films = curs.fetchall()
    finally:
        conn.close()
    return render_template('films.html', username=username, films=films)


@app.route('/profile/actors')
def show_actors():
    username = get_cookie()
    conn = dbconnect.connect()
    try:
        with conn.cursor() as curs:
            curs.execute('SELECT actor_id, first_name, last_name FROM actor ORDER BY last_name ;')
            actors = curs.fetchall()
    finally:
        conn.close()
    return render_template('actors.html', username=username, actors=actors)


@app.route('/profile/films/<int:film_id>')
def film_info(film_id):
    username = get_cookie()
    return 'film information'


if "__name__" == "__main__":
    app.run("0.0.0.0", 5000)
