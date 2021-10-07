from flask import Blueprint, render_template
from flask_login.utils import login_required
'''
    Note that in the below code,
    some arguments are specified when creating the Blueprint object
    The first argument, 'site', is the Blueprint's name,
    which is used by Flask's routing mechanism.
    The Second argument, __name__, is the Blueprint's import name,
    which Flask uses to locate the Blueprint's resources.    
'''
site = Blueprint('site', __name__, template_folder ='site_templates')
@site.route('/')
def home():
    return render_template('home.html')
@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
@site.route('/classes')
def classes():
    return render_template('classes.html')