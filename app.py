from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("love.html")

@app.route("/yes")
def yes():
    return render_template("yes.html")

# Render uses gunicorn, not app.run()
