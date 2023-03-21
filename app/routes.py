
from app import app


@app.route('/home')
def homePage():
    return {
        'Oh hello there': 'CLUTCH!'
    }

@app.route('/')
def landingPage():
    return {
        'You\'ve landed!': 'I hope it was a good flight'
    }

@app.route('/test')
def testPage():
    return {
        'TESTINGTESTING': '123'
    }
