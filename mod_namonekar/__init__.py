from flask import Blueprint , render_template

nemone_kar = Blueprint('nemone_kar',__name__,url_prefix='/nemone_kar/')

@nemone_kar.route('/')
def index():
    return render_template('nemone_kar.html')
