from flask import Blueprint , render_template

khadamati = Blueprint('khadamati',__name__,url_prefix='/khadamati')

@khadamati.route('/')
def index():
    return render_template('khadamati/khadamati.html')

@khadamati.route('/khadamat_choob')
def khadamat_choob():
    return render_template('khadamati/khadamat_choob.html')

@khadamati.route('/khadamat_mdf')
def khadamat_mdf():
    return render_template('khadamati/khadamat_mdf.html')
