from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .forms import CreatePostForm
from ..models import Post

ig = Blueprint('ig', __name__, template_folder='ig_templates')

@ig.route('/posts/create', methods=['GET', 'POST'])
@login_required
def createPost():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            body = form.body.data

            new = Post(title, img_url, body, current_user.id)
            new.savePost()
            print('NEW POST MADE!!!!')
            return redirect(url_for('homePage'))

    return render_template('create_post.html', form=form)

@ig.route('/posts/feed')
@login_required
def feed():
    posts = Post.query.all()
    print(posts)
    return render_template('feed.html', posts=posts)


