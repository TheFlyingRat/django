from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
  {
    'name': 'Apple',
    'amount': 4,
    'price': 0.9,
  },
  {
    'name': 'Banana',
    'amount': 9,
    'price': 1.2,
  },
  {
    'name': 'Coconut',
    'amount': 2,
    'price': 2.1,
  },
]

@app.route('/')
def index():
  return render_template('index.html', products=PRODUCTS)