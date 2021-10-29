from flask import Flask, render_template, \
    request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import User, Product
products = []

@app.route('/')
def home():
    return render_template('home.html', products=products)


@app.route('/about')
def about_page():
    return "This is the about page"


@app.route('/add-new-product')
def add_product_page():
    return render_template('add-product.html')


@app.route('/add-product', methods=['POST', 'GET'])
def add_product():
    if request.method == 'GET':
        return redirect(url_for('add_product_page'))
    else:
        title = request.form['title']
        category = request.form['category']
        price = request.form['price']
        description = request.form['description']

        products.append(
            {
                "title": title,
                "price": price,
                "category": category,
                "description": description
             }
        )
        return redirect(url_for('home'))

