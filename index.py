from flask import Flask, render_template, \
    request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import User, Product


@app.route('/')
def home():
    products = Product.query.all()
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

        # create product object
        product = Product(title=title, category=category,
                          price=price, description=description)
        db.session.add(product)
        db.session.commit()
        flash('{} added successfully.'.format(title))
        return redirect(url_for('home'))


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_product(id):
    # check database for the product with that id.
    product = Product.query.filter(Product.id == id).one()
    if product is None:
        # if the product was not found send msg and redirect
        flash('Product not found')
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('edit.html', product=product)
    else:
        # update the product
        if request.form['title'] == '':
            flash('Please enter product title.')
            return render_template('edit.html', product=product)

        product.title = request.form['title']
        product.price = request.form['price']
        product.category = request.form['category']
        product.description = request.form['description']
        db.session.commit()
        flash('Product updated successfully')
        return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete_product(id):
    # check database for the product with that id.
    product = Product.query.filter(Product.id == id).one()
    if product is None:
        # if the product was not found send msg and redirect
        flash('Product not found')
        return redirect(url_for('home'))
    else:
        db.session.delete(product)
        db.session.commit()
        flash('{} deleted successfully'.format(product.title))
        return redirect(url_for('home'))
