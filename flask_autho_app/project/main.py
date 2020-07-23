from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


# function to protect a page when using Flask-login using @login_required between route and function
# This prevents user who is not logged in from seeing the route
# If user is not logged in, the user will get redirected to the login page, per the Flask-login configuration
# Routes decorated with @login_required have ability to use current_user object inside of function
# Current user represents user form database, we can access all attributes of that user with dot notation
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/profile')
def profile():
    return render_template('profile.html')
