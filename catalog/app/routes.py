from flask import render_template
from app import app

@app.route('/')
def home():
	return render_template('home.html', businessname = "Hour Watches Homepage", slogan = "Vintage Watch Shop")

@app.route('/catalog')
def catalog():
	return "Placeholder for Watches"

@app.route('/jewelry')
def jewelry():
    return "Placeholder for Jewelry"

@app.route('/bags')
def bags():
    return "Placeholder for Bags"
