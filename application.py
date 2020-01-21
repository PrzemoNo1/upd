from flask import Flask
from create import start_creating
app = Flask(__name__)

@app.route("/")
def hello():
    start_creating()
    return "Hello World!"