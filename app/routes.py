
from app import app

from flask import render_template, request, url_for, redirect
from .forms import SignUpForm
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

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)

            user = User(username, email, password)            
            user.saveUser()
            return redirect(url_for('loginPage'))


    return render_template('register.html', form=form)
