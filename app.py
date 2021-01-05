from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app , db)



@app.route('/')
def index():
    return render_template('index.html')

from mod_users import users
app.register_blueprint(users)

from mod_admin import admin
app.register_blueprint(admin)

from mod_namonekar import nemone_kar
app.register_blueprint(nemone_kar)


from mod_registerwork import register_work
app.register_blueprint(register_work)


from mod_khadamati import khadamati
app.register_blueprint(khadamati)