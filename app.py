from flask import Flask, render_template

app = Flask(__name__)

NAME = "app"

@app.route('/')
def index():
  return render_template('index.html', name=NAME)