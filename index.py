from flask import Flask, render_template

app = Flask(__name__)

name = 'Jon'
age = 90
products = [
    {
        "title": "Samsung S20",
        "price": 20000,
        "category": 'smart phones',
        "description": "Album example is © Bootstrap, but please download and customize it for yourself!"
    },
    {
        "title": "iPhone 22",
        "price": 5920000,
        "category": 'smart phones',
        "description": "Album example is © Bootstrap, but please download and customize it for yourself!"
    },
    {
        "title": "Samsung XYZ",
        "price": 3420000,
        "category": 'smart phones',
        "description": "Album example is © Bootstrap, but please download and customize it for yourself!"
    }
]


fruits = ['Mango', 'Banana', 'Orange', 'Apple']

@app.route('/')
def home():
    new_fruit = 'Grape'
    fruits.append(new_fruit)

    return render_template('home.html', my_friuts=fruits, products=products)


@app.route('/about')
def about_page():
    return "This is the about page"


@app.route('/test')
def test_page():
    x = 200
    y = 240
    ans = "The result of py function is " + str(y % x)
    return ans
