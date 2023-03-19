from flask import Flask, render_template, request
import main
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/log")
def log():
    return main.flasklog(request.args.get("msg"))
@app.route("/res")
def res():
    return main.user(request.args.get('inp'),bool(request.args.get('how_just')),bool(request.args.get('how_rate')))