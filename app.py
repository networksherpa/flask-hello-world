# --- Flask Hello World --- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
