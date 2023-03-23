
from app import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

from .auth.forms import SignUpForm, LoginForm
from .models import User

@app.route('/')
def homePage():
    teachers = [
        {
        'name': 'Brendan',
        'age': 456,
        'spec' : 'Vim'
        },
        {
        'name': 'Rachel',
        'age' : 342,
        'spec' : 'student relations'
        },
        {
        'name' : 'Brandt',
        'age' : 567,
        'spec': 'none'
        }
    ]
    fav_animal = 'Tiger'
    return render_template('index.html', teachers=teachers, f = fav_animal)




