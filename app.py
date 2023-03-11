from flask import Flask, render_template, request
import main
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/res")
def res():
    return main.user(request.args.get('inp'),bool(request.args.get('how_just')))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)