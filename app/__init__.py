from flask import Flask
from flask_bcrypt import Bcrypt
from myblueprint import new_page

app = Flask(__name__)
app.register_blueprint(new_page, url_prefix='/new_page')

bcrypt = Bcrypt(app)
