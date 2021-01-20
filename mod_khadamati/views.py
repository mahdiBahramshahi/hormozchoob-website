from flask.helpers import url_for
from sqlalchemy.sql.elements import Null
from wtforms.validators import DataRequired
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

@khadamati.route('/khadamat_mdf' ,methods=['GET','POST'])
def khadamat_mdf():
    if not session.get('email'):
        flash('شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', 'error')
        return redirect(url_for('users.login'))
    form = FileUploadForm()
    if request.method == 'POST' :
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید','error')
            return redirect(url_for('users.login')) 
            
        # if not form.validate_on_submit():
        #     abort(400)

        session['project_name'] = request.form.get('project_name')

        old_projectname = File.query.filter(File.project_name.ilike(form.project_name.data)).first()
        if old_projectname:
            flash('نام پروژه تکراری میباشد' , 'error')
            return render_template('khadamati/khadamat_mdf.html')
            
    if session.get('project_name') is not None:
        flash("پروژه با موفقیت ساخته شد", category='')
        return redirect(url_for('khadamati.kh_cut'))
    
    return render_template('khadamati/khadamat_mdf.html')




@khadamati.route('/pvc')
def kh_pvc():
    return render_template('khadamati/kh_pvc.html')




@khadamati.route('/cut' ,methods=['GET','POST'])
def kh_cut():
    if not session.get('email'):
        flash('شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', 'error')
        return redirect(url_for('users.login')) 
    form = FileUploadForm()
    if request.method == 'POST' :
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید','error')
            return redirect(url_for('users.login')) 
        if not form.validate_on_submit():
            abort(400)
        
        filename = f'{uuid.uuid1()}_{ secure_filename(form.file.data.filename)}'
        username = session.get('username')
        new_file = File()
        new_file.project_name = session.get('project_name')
        new_file.username = username
        new_file.height = form.height.data
        new_file.width = form.width.data
        new_file.qty = form.qty.data
        new_file.pvc = form.pvc.data
        new_file.filename = filename
        
        # session['height'] = form.height.data
        # session['width'] = form.width.data
        # session['qty'] = form.qty.data
        # session['pvc'] = form.pvc.data
        
        # old_projectname = File.query.filter(File.project_name.ilike)
        # (File.project_name.ilike(form.project_name.data)).first()
        # old_projectname = File.query.filter(File.project_name.ilike(form.project_name.data))
        # print(old_projectname)
        try:
            db.session.add(new_file)
            db.session.commit()
            form.file.data.save(f'static/uploads/khadamati/cut/{filename}')
            flash('سفارش ثبت شد')
            return redirect(url_for('khadamati.kh_cut'))
        except IntegrityError:
            flash('!سفارش ثبت نشد' , 'error')
            return redirect(url_for('khadamati.khadamat_mdf'))
    if session.get('project_name'):

        project_name = File.query.filter(File.project_name == session.get('project_name'))

        try:
            number_1 = project_name[0]
            number_2 = project_name[1]
            number_3 = project_name[2]
            number_4 = project_name[3]
            number_5 = project_name[4]
            number_6 = project_name[5]
            number_7 = project_name[6]
            number_8 = project_name[7]
            number_9 = project_name[8]
            number_10 = project_name[9]
            number_11 = project_name[10]
            number_12 = project_name[11]
            number_13 = project_name[12]
            number_14 = project_name[13]
            number_15 = project_name[14]
            number_16 = project_name[15]
            number_17 = project_name[16]
            number_18 = project_name[17]
            number_19 = project_name[18]
            number_20 = project_name[19]
            number_21 = project_name[21]
            number_22 = project_name[21]
            number_23 = project_name[22]
            number_24 = project_name[23]
            number_25 = project_name[24]
            number_26 = project_name[25]
            number_27 = project_name[26]
            number_28 = project_name[27]
            number_29 = project_name[28]
            number_30 = project_name[29]
            number_31 = project_name[30]
            number_32 = project_name[31]
            number_33 = project_name[32]
            number_34 = project_name[33]
            number_35 = project_name[34]
            number_36 = project_name[35]
            number_37 = project_name[36]
            number_38 = project_name[37]
            number_39 = project_name[38]
            number_40 = project_name[39]
            number_41 = project_name[40]
            number_42 = project_name[41]
            number_43 = project_name[42]
            number_44 = project_name[43]
            number_45 = project_name[44]
            number_46 = project_name[45]
            number_47 = project_name[46]
            number_48 = project_name[47]
            number_49 = project_name[48]
            number_50 = project_name[49]

        except IndexError:
            pass
        # try:
        #     if number_1 is not None:
        #         width_1 = number_1.width
        #     if number_2 is not None:
        #         width_2 = number_2.width
            
        # except UnboundLocalError:
        #     width_2 = 'ثبت نشده'








        # ================================ height ==============================






        try:   
            height_1 = number_1.height    
        except UnboundLocalError:
            height_1 = "وارد نشده"

        try:   
            height_2 = number_2.height    
        except UnboundLocalError:
            height_2 = "وارد نشده"
        
        try:   
            height_3 = number_3.height    
        except UnboundLocalError:
            height_3 = "وارد نشده"
        
        try:   
            height_4 = number_4.height    
        except UnboundLocalError:
            height_4 = "وارد نشده"
        
        try:   
            height_5 = number_5.height    
        except UnboundLocalError:
            height_5 = "وارد نشده"
        
        try:   
            height_6 = number_6.height    
        except UnboundLocalError:
            height_6 = "وارد نشده"
        
        try:   
            height_7 = number_7.height    
        except UnboundLocalError:
            height_7 = "وارد نشده"
        
        try:   
            height_8 = number_8.height    
        except UnboundLocalError:
            height_8 = "وارد نشده"
        try:   
            height_9 = number_9.height    
        except UnboundLocalError:
            height_9 = "وارد نشده"
        
        try:   
            height_10 = number_10.height    
        except UnboundLocalError:
            height_10 = "وارد نشده"
        
        try:   
            height_11 = number_11.height    
        except UnboundLocalError:
            height_11 = "وارد نشده"
        
        try:   
            height_12 = number_12.height    
        except UnboundLocalError:
            height_12 = "وارد نشده"
        
        try:   
            height_13 = number_13.height    
        except UnboundLocalError:
            height_13 = "وارد نشده"
        
        try:   
            height_14 = number_14.height    
        except UnboundLocalError:
            height_14 = "وارد نشده"
        
        try:   
            height_15 = number_15.height    
        except UnboundLocalError:
            height_15 = "وارد نشده"
        
        try:   
            height_16 = number_16.height    
        except UnboundLocalError:
            height_16 = "وارد نشده"
        
        try:   
            height_17 = number_17.height    
        except UnboundLocalError:
            height_17 = "وارد نشده"
        
        try:   
            height_18 = number_18.height    
        except UnboundLocalError:
            height_18 = "وارد نشده"
        
        try:   
            height_19 = number_19.height    
        except UnboundLocalError:
            height_19 = "وارد نشده"
        
        try:   
            height_20 = number_20.height    
        except UnboundLocalError:
            height_20 = "وارد نشده"
        
        




        # ================================ width ===============================






        try:
            width_1 = number_1.width   
        except UnboundLocalError:
            width_1 = "وارد نشده"
        
        try:   
            width_2 = number_2.width    
        except UnboundLocalError:
            width_2 = "وارد نشده"
        
        try:   
            width_3 = number_3.width    
        except UnboundLocalError:
            width_3 = "وارد نشده"
        
        try:   
            width_4 = number_4.width    
        except UnboundLocalError:
            width_4 = "وارد نشده"
        
        try:   
            width_5 = number_5.width    
        except UnboundLocalError:
            width_5 = "وارد نشده"
        
        try:   
            width_6 = number_6.width    
        except UnboundLocalError:
            width_6 = "وارد نشده"
        
        try:   
            width_7 = number_7.width    
        except UnboundLocalError:
            width_7 = "وارد نشده"
        
        try:   
            width_8 = number_8.width    
        except UnboundLocalError:
            width_8 = "وارد نشده"
        try:   
            width_9 = number_9.width    
        except UnboundLocalError:
            width_9 = "وارد نشده"
        
        try:   
            width_10 = number_10.width    
        except UnboundLocalError:
            width_10 = "وارد نشده"
        
        try:   
            width_11 = number_11.width    
        except UnboundLocalError:
            width_11 = "وارد نشده"
        
        try:   
            width_12 = number_12.width    
        except UnboundLocalError:
            width_12 = "وارد نشده"
        
        try:   
            width_13 = number_13.width    
        except UnboundLocalError:
            width_13 = "وارد نشده"
        
        try:   
            width_14 = number_14.width    
        except UnboundLocalError:
            width_14 = "وارد نشده"
        
        try:   
            width_15 = number_15.width    
        except UnboundLocalError:
            width_15 = "وارد نشده"
        
        try:   
            width_16 = number_16.width    
        except UnboundLocalError:
            width_16 = "وارد نشده"
        
        try:   
            width_17 = number_17.width    
        except UnboundLocalError:
            width_17 = "وارد نشده"
        
        try:   
            width_18 = number_18.width    
        except UnboundLocalError:
            width_18 = "وارد نشده"
        
        try:   
            width_19 = number_19.width   
        except UnboundLocalError:
            width_19 = "وارد نشده"
        
        try:   
            width_20 = number_20.width    
        except UnboundLocalError:
            width_20 = "وارد نشده"
        
        
        # ================================ qty ===============================
        try:
            qty_1 = number_1.qty   
        except UnboundLocalError:
            qty_1 = "وارد نشده"

        
        try:   
            qty_2 = number_2.qty    
        except UnboundLocalError:
            qty_2 = "وارد نشده"
        
        try:   
            qty_3 = number_3.qty   
        except UnboundLocalError:
            qty_3 = "وارد نشده"
        
        try:   
            qty_4 = number_4.qty    
        except UnboundLocalError:
            qty_4 = "وارد نشده"
        
        try:   
            qty_5 = number_5.qty    
        except UnboundLocalError:
            qty_5 = "وارد نشده"
        
        try:   
            qty_6 = number_6.qty    
        except UnboundLocalError:
            qty_6 = "وارد نشده"
        
        try:   
            qty_7 = number_7.qty    
        except UnboundLocalError:
            qty_7 = "وارد نشده"
        
        try:   
            qty_8 = number_8.qty    
        except UnboundLocalError:
            qty_8 = "وارد نشده"
        try:   
            qty_9 = number_9.qty    
        except UnboundLocalError:
            qty_9 = "وارد نشده"
        
        try:   
            qty_10 = number_10.qty    
        except UnboundLocalError:
            qty_10 = "وارد نشده"
        
        try:   
            qty_11 = number_11.qty    
        except UnboundLocalError:
            qty_11 = "وارد نشده"
        
        try:   
            qty_12 = number_12.qty    
        except UnboundLocalError:
            qty_12 = "وارد نشده"
        
        try:   
            qty_13 = number_13.qty    
        except UnboundLocalError:
            qty_13 = "وارد نشده"
        
        try:   
            qty_14 = number_14.qty    
        except UnboundLocalError:
            qty_14 = "وارد نشده"
        
        try:   
            qty_15 = number_15.qty    
        except UnboundLocalError:
            qty_15 = "وارد نشده"
        
        try:   
            qty_16 = number_16.qty    
        except UnboundLocalError:
            qty_16 = "وارد نشده"
        
        try:   
            qty_17 = number_17.qty    
        except UnboundLocalError:
            qty_17 = "وارد نشده"
        
        try:   
            qty_18 = number_18.qty    
        except UnboundLocalError:
            qty_18 = "وارد نشده"
        
        try:   
            qty_19 = number_19.qty   
        except UnboundLocalError:
            qty_19 = "وارد نشده"
        
        try:   
            qty_20 = number_20.qty    
        except UnboundLocalError:
            qty_20 = "وارد نشده"
        
        
        # ================================ pvc ===============================

        try:
            pvc_1 = number_1.pvc   
        except UnboundLocalError:
            pvc_1 = "وارد نشده"
        
        try:
            pvc_1 = number_1.pvc   
        except UnboundLocalError:
            pvc_1 = "وارد نشده"
        
        try:   
            pvc_2 = number_2.pvc    
        except UnboundLocalError:
            pvc_2 = "وارد نشده"
        
        try:   
            pvc_3 = number_3.pvc    
        except UnboundLocalError:
            pvc_3 = "وارد نشده"
        
        try:   
            pvc_4 = number_4.pvc    
        except UnboundLocalError:
            pvc_4 = "وارد نشده"
        
        try:   
            pvc_5 = number_5.pvc    
        except UnboundLocalError:
            pvc_5 = "وارد نشده"
        
        try:   
            pvc_6 = number_6.pvc    
        except UnboundLocalError:
            pvc_6 = "وارد نشده"
        
        try:   
            pvc_7 = number_7.pvc    
        except UnboundLocalError:
            pvc_7 = "وارد نشده"
        
        try:   
            pvc_8 = number_8.pvc    
        except UnboundLocalError:
            pvc_8 = "وارد نشده"
        try:   
            pvc_9 = number_9.pvc    
        except UnboundLocalError:
            pvc_9 = "وارد نشده"
        
        try:   
            pvc_10 = number_10.pvc    
        except UnboundLocalError:
            pvc_10 = "وارد نشده"
        
        try:   
            pvc_11 = number_11.pvc    
        except UnboundLocalError:
            pvc_11 = "وارد نشده"
        
        try:   
            pvc_12 = number_12.pvc    
        except UnboundLocalError:
            pvc_12 = "وارد نشده"
        
        try:   
            pvc_13 = number_13.pvc    
        except UnboundLocalError:
            pvc_13 = "وارد نشده"
        
        try:   
            pvc_14 = number_14.pvc    
        except UnboundLocalError:
            pvc_14 = "وارد نشده"
        
        try:   
            pvc_15 = number_15.pvc    
        except UnboundLocalError:
            pvc_15 = "وارد نشده"
        
        try:   
            pvc_16 = number_16.pvc    
        except UnboundLocalError:
            pvc_16 = "وارد نشده"
        
        try:   
            pvc_17 = number_17.pvc    
        except UnboundLocalError:
            pvc_17 = "وارد نشده"
        
        try:   
            pvc_18 = number_18.pvc    
        except UnboundLocalError:
            pvc_18 = "وارد نشده"
        
        try:   
            pvc_19 = number_19.pvc   
        except UnboundLocalError:
            pvc_19 = "وارد نشده"
        
        try:   
            pvc_20 = number_20.pvc    
        except UnboundLocalError:
            pvc_20 = "وارد نشده"


    if not session.get('project_name'):
        flash('شما پروژه تان را نساخته اید')
        return redirect(url_for('khadamati.khadamat_mdf'))
        
        

    
    # try:
    return render_template('khadamati/kh_cut.html' , form=form ,
     width_1=width_1 ,height_1=height_1 , qty_1=qty_1 , pvc_1=pvc_1 ,
     width_2=width_2 ,height_2=height_2 , qty_2=qty_2 , pvc_2=pvc_2 ,
     width_3=width_3 ,height_3=height_3 , qty_3=qty_3 , pvc_3=pvc_3 ,
     width_4=width_4 ,height_4=height_4 , qty_4=qty_4 , pvc_4=pvc_4 ,
     width_5=width_5 ,height_5=height_5 , qty_5=qty_5 , pvc_5=pvc_5 ,
     width_6=width_6 ,height_6=height_6 , qty_6=qty_6 , pvc_6=pvc_6 ,
     width_7=width_7 ,height_7=height_7 , qty_7=qty_7 , pvc_7=pvc_7 ,
     width_8=width_8 ,height_8=height_8 , qty_8=qty_8 , pvc_8=pvc_8 ,
     width_9=width_9 ,height_9=height_9 , qty_9=qty_9 , pvc_9=pvc_9 ,
     width_10=width_10 ,height_10=height_10 , qty_10=qty_10 , pvc_10=pvc_10 ,
     width_11=width_11 ,height_11=height_11 , qty_11=qty_11 , pvc_11=pvc_11 ,
     width_12=width_12 ,height_12=height_12 , qty_12=qty_12 , pvc_12=pvc_12 ,
     width_13=width_13 ,height_13=height_13 , qty_13=qty_13 , pvc_13=pvc_13 ,
     width_14=width_14 ,height_14=height_14 , qty_14=qty_14 , pvc_14=pvc_14 ,
     width_15=width_15 ,height_15=height_15 , qty_15=qty_15 , pvc_15=pvc_15 ,
     width_16=width_16 ,height_16=height_16 , qty_16=qty_16 , pvc_16=pvc_16 ,
     width_17=width_17 ,height_17=height_17 , qty_17=qty_17 , pvc_17=pvc_17 ,
     width_18=width_18 ,height_18=height_18 , qty_18=qty_18 , pvc_18=pvc_18 ,
     width_19=width_19 ,height_19=height_19 , qty_19=qty_19 , pvc_19=pvc_19 ,
     width_20=width_20 ,height_20=height_20 , qty_20=qty_20 , pvc_20=pvc_20 ,
    )
    # except UnboundLocalError:
    #     pass
