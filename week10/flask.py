from flask import flask

app = flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
