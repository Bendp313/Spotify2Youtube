from flask import Flask, render_template, request
import main
from waitress import serve
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/run", methods=["POST", "GET"])
def run():
    playlist_link = request.form["pl_input"]
    main.start(playlist_link)

if __name__ in "__main__":
   serve(app, host="0.0.0.0", port=8000) 