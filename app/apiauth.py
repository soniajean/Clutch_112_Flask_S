from functools import wraps
from flask import request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import check_password_hash

from app.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    
@token_auth.verify_token
def verify_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        return user

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:]
        else:
            return {
                'status' : 'NOT ok',
                'message' : 'Missing required parameter "Authorization" from headers'
            }
        if not token:
            return {
                'status' : 'NOT ok',
                'message' : 'Missing auth token, please provide'
            }
        user = User.query.filter_by(token=token).first()
        if not user:
            return {
                'status' : 'NOT ok',
                'message' : 'Token does not belong to a valid user'
            }
        return func(user=user, *args, **kwargs)
    return decorated