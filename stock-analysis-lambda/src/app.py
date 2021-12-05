import flask

app = flask.Flask(__name__)


@app.route("/")
def welcome_():
    return "Example setup for the stock analysis"


if __name__ == "__main__":
    app.run()
