from flask import Flask
import create
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    create.start_creating()