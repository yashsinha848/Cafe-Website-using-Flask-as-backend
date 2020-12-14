from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy


local_server = True
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/products.html")
def products():
    return render_template('products.html')

@app.route("/store.html")
def store():
    return render_template('store.html')
app.run(debug=True)