from flask import Flask
from create import start_creating
app = Flask(__name__)

@app.route("/")
def hello():
    print("Poczatek")
    start_creating()
    return "Hello World!"