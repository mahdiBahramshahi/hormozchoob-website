from flask import request , render_template , flash , session , abort , redirect , url_for
from flask_wtf import form
from .models import User 
from app import db
from .forms import RegisterForm , LoginForm
from mod_uploads.forms import FileUploadForm
from mod_uploads.models import File, kh_project
from werkzeug.utils import secure_filename
import uuid
from sqlalchemy.exc import IntegrityError

from . import users

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)
        if not form.password.data == form.confirm_password.data:
            error_msg = 'Password and Confirm Password does not match.'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
            return render_template('users/register.html', form=form)
        old_username = User.query.filter(User.username.ilike(form.username.data)).first()
        if old_username:
            flash('نام کاربری تکراری میباشد' , 'error')
            return render_template('users/register.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('ایمیل تکراری می باشد' , 'error')
            return render_template('users/register.html', form=form)

        

        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        new_user.phone_number = form.phone_number.data
        db.session.add(new_user)
        db.session.commit()
        
        flash('ثبت نام با موفقیت انجام شد' , 'success')
        return redirect(url_for('users.login'))
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('Email is in use.' , 'error')
    return render_template('users/register.html', form=form)




@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f"{form.email.data}")).first()

        if not user:
            flash("شما ثبت نام نکرده اید", category='error')
            return render_template('users/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("نام کاربری / رمز ورود  نادرست است", category='error')
            return render_template('users/login.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='error')
        #     return(redirect(url_for('index')))
        
        session['email'] = user.email
        session['user_id'] = user.id
        session['username'] = user.username

        # return redirect(url_for('index'))
    if session.get('email') is not None:
        flash("ورود با موفقیت انجام شد", category='')
        return redirect(url_for('index'))
    return render_template('users/login.html', form=form)




@users.route('/logout/', methods = ['GET'])
def logout():
    if session.get('email'):
        session.clear()
        flash('با موفقیت خارج شدید' , 'warning')
        return(redirect(url_for('users.login')))
        
    flash('شما وارد نشده اید' , 'warning')
    return(redirect(url_for('users.login')))





# @users.route('/upload',  methods= ['GET','POST'])
# def upload_file():
#     form = FileUploadForm()
#     if request.method == 'POST':
#         if not form.validate_on_submit():
#             abort(400)
#         filename = f'{uuid.uuid1()}_{ secure_filename(form.file.data.filename)}'
#         new_file = File()
#         new_file.filename = filename
#         try:
#             db.session.add(new_file)
#             db.session.commit()
#             form.file.data.save(f'static/uploads/khadamati/cut/{filename}')
#             flash('فایل آپلود شد')
#         except IntegrityError:
#             flash('!فایل آپلود نشد' , 'error')

#     return render_template('users/upload_file.html' , form=form)




@users.route('/my_projects',  methods= ['GET','POST'])
def my_projects():
    if not session.get('email'):
        flash('شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', 'error')
        return redirect(url_for('users.login')) 
    my_projects = kh_project.query.order_by(kh_project.id.desc()).filter(kh_project.username == session.get('username')).all()
    return render_template('users/my_projects.html' , my_projects=my_projects)
    
@users.route('/<string:slug>')
def single_project(slug):
    project = kh_project.query.filter(kh_project.slug == slug).first_or_404()
    project_name = File.query.filter(File.project_name == project.project_name)



    return render_template('users/single_project.html' , project=project , project_name=project_name)
