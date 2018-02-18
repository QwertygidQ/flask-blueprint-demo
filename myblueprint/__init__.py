from flask import Blueprint
#from app import bcrypt

new_page = Blueprint('new_page', __name__, template_folder='templates')

from . import views