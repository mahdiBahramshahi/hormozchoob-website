from flask import Blueprint 

khadamati = Blueprint('khadamati',__name__,url_prefix='/khadamati')

from . import views
