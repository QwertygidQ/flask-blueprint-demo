from flask import render_template
from . import new_page


@new_page.route('/')
def index():
    return render_template('index.html',
                           title='My Home Page',
                           msg='Hello, world!')