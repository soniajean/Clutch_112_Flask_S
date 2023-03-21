
from app import app

from flask import render_template


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')
