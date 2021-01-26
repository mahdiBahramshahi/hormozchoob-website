from flask.helpers import url_for
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.functions import user
from wtforms.validators import DataRequired
from . import khadamati
from mod_users.models import User
from  mod_users.forms import RegisterForm, LoginForm

from flask import  render_template , abort , request , flash , session
import uuid
from mod_uploads.forms import FileUploadForm
from mod_uploads.models import File , kh_project
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
        return redirect(url_for('khadamati.login'))
    form = FileUploadForm()
    if request.method == 'POST' :
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید','error')
            return redirect(url_for('khadamati.login')) 
            
        # if not form.validate_on_submit():
        #     abort(400)

        # session.pop('project_name')
        session['project_name'] = request.form.get('project_name')

        old_projectname = File.query.filter(File.project_name.ilike(form.project_name.data)).first()
        if old_projectname:
            flash('نام پروژه تکراری میباشد' , 'error')
            return render_template('khadamati/khadamat_mdf.html')
        
        


    # if session.get('project_name') is not None:
    #     try:
    #         username = session.get('username')
    #         name_of_projects = kh_project()
    #         name_of_projects.project_name = request.form.get('project_name')
    #         name_of_projects.username = username
    #         name_of_projects.slug = f"{name_of_projects.project_name}"
    #         db.session.add(name_of_projects)
    #         db.session.commit()
    #     except IntegrityError:
    #         flash('نام پروژه تکراری میباشد' , 'error')
    #         return render_template('khadamati/khadamat_mdf.html')

        flash("پروژه با موفقیت ساخته شد", category='')
        return redirect(url_for('khadamati.kh_cut'))
    
    return render_template('khadamati/khadamat_mdf.html')




@khadamati.route('/pvc')
def kh_pvc():
    return render_template('khadamati/kh_pvc.html')





@khadamati.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('khadamati/register.html', form=form)
        if not form.password.data == form.confirm_password.data:
            error_msg = 'Password and Confirm Password does not match.'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
            return render_template('khadamati/register.html', form=form)
        old_username = User.query.filter(User.username.ilike(form.username.data)).first()
        if old_username:
            flash('نام کاربری تکراری میباشد' , 'error')
            return render_template('khadamati/register.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('ایمیل تکراری می باشد' , 'error')
            return render_template('khadamati/register.html', form=form)

        

        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        
        flash('ثبت نام با موفقیت انجام شد' , 'success')
        return redirect(url_for('khadamati.login'))
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('Email is in use.' , 'error')
    return render_template('khadamati/register.html', form=form)






@khadamati.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f"{form.email.data}")).first()

        if not user:
            flash("شما ثبت نام نکرده اید", category='error')
            return render_template('khadamati/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("نام کابری / رمز ورود  نادرست است", category='error')
            return render_template('khadamati/login.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='error')
        #     return(redirect(url_for('index')))
        
        session['email'] = user.email
        session['user_id'] = user.id
        session['username'] = user.username

        # return redirect(url_for('index'))
    if session.get('email') is not None:
        flash("ورود با موفقیت انجام شد", category='')
        return redirect(url_for('khadamati.khadamat_mdf'))
    return render_template('khadamati/login.html', form=form)








@khadamati.route('/cut' ,methods=['GET','POST'])
def kh_cut():
    if not session.get('email'):
        flash('شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', 'error')
        return redirect(url_for('khadamati.login')) 
    form = FileUploadForm()
    if request.method == 'POST' :
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید','error')
            return redirect(url_for('khadamati.login')) 
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
        new_file.mdf_model = form.mdf_model.data
        new_file.Charkhesh = form.Charkhesh.data
        new_file.shiar = form.shiar.data
        new_file.farsi = form.farsi.data
        new_file.about = form.about.data
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
        
    
    # project_name = File.query.filter(File.project_name == session.get('project_name'))
    # tables= kh_project.query.order_by(kh_project.id.desc()).all()
    

    if not session.get('project_name'):
        flash('شما پروژه تان را نساخته اید' , 'error')
        return redirect(url_for('khadamati.khadamat_mdf'))
        
        

    
    # try:
    return render_template('khadamati/kh_cut.html' , form=form , project_name=project_name)


@khadamati.route('/register_project' ,methods=['GET'])
def register_end():
    if session.get('project_name'):
        project_name = File.query.filter(File.project_name == session.get('project_name')) 
    if project_name:
        if session.get('project_name') is not None:
            try:
                username = session.get('username')
                name_of_projects = kh_project()
                name_of_projects.project_name = session.get('project_name')
                name_of_projects.username = username
                name_of_projects.slug = f"{name_of_projects.project_name}"
                db.session.add(name_of_projects)
                db.session.commit()
            except IntegrityError:
                flash('!پروژه ثبت نشد' , 'error')
                return render_template('khadamati/khadamat_mdf.html')
            flash('سفارش با موفقیت ثبت شد ')
            session.pop('project_name')
        return redirect(url_for('khadamati.khadamat_mdf'))
    return redirect(url_for('khadamati.khadamat_mdf')) 

