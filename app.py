from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    """ This is the main page of the file """
    return 'hello'