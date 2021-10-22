from flask import Flask, render_template

app = Flask(__name__)

name = 'Jon'
age = 90

@app.route('/')
def home():
    return render_template('home.html', name=name, how_old=age)


@app.route('/about')
def about_page():
    return "This is the about page"


@app.route('/test')
def test_page():
    x = 200
    y = 240
    ans = "The result of py function is " + str(y % x)
    return ans
