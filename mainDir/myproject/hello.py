from flask import Flask

app = Flask(__name__)

@app.route("/")

def hellow_world():
    return "<p><small>Hellow, World!</small><br><h1>come on are you for real?</h1></p>"