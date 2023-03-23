from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    img_url = StringField('Image URL')
    body = StringField('Body')
    submit = SubmitField()





