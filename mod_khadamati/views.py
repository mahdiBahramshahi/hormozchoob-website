from flask.helpers import url_for
from . import khadamati

from flask import  render_template , abort , request , flash , session
import uuid
from mod_uploads.forms import FileUploadForm
from mod_uploads.models import File
from werkzeug.utils import redirect, secure_filename
from app import db
from sqlalchemy.exc import IntegrityError



@khadamati.route('/')
def index():
    return render_template('khadamati/khadamati.html')

@khadamati.route('/khadamat_choob')
def khadamat_choob():
    return render_template('khadamati/khadamat_choob.html')

@khadamati.route('/khadamat_mdf')
def khadamat_mdf():
    return render_template('khadamati/khadamat_mdf.html')

@khadamati.route('/pvc')
def kh_pvc():
    return render_template('khadamati/kh_pvc.html')




@khadamati.route('/cut' ,methods=['GET','POST'])
def kh_cut():
    form = FileUploadForm()
    if request.method == 'POST' :
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید','error')
            return redirect(url_for('users.login')) 
        if not form.validate_on_submit():
            abort(400)
        filename = f'{uuid.uuid1()}_{ secure_filename(form.file.data.filename)}'
        new_file = File()
        new_file.filename = filename
        try:
            db.session.add(new_file)
            db.session.commit()
            form.file.data.save(f'static/uploads/khadamati/cut/{filename}')
            flash('فایل آپلود شد')
        except IntegrityError:
            flash('!فایل آپلود نشد' , 'error')


    return render_template('khadamati/kh_cut.html' , form=form)