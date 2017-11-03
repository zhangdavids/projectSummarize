import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))



@app.route('/')
def hello():
    return "Hello world"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
