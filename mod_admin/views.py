from flask import session , render_template , request , abort , flash , redirect, url_for
from mod_users.forms import LoginForm , RegisterForm
from mod_users.models import User
from .import admin
from .utils import admin_only_view
from mod_uploads.models import File, kh_project
from app import db

@admin.route('/')
@admin_only_view
def index():
    return render_template('admin/index.html')

@admin.route('/login/',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f"{form.email.data}")).first()

        if not user:
            flash("ورود نامعتبر است", category='error')
            return render_template('admin/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("ورود نامعتبر است", category='error')
            return render_template('admin/login.html', form=form)

        if not user.is_admin():
            flash("ورود نامعتبر است", category='error')
            return render_template('admin/login.html', form=form)
        
        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role        
        return redirect(url_for('admin.index'))
    if session.get('role') == 1:
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)




@admin.route('/logout/', methods = ['GET'])
@admin_only_view
def logout():
    if session.get('email'):
        session.clear()
        flash('با موفقیت خارج شدید' , 'warning')
        return(redirect(url_for('admin.login')))
        
    flash('شما وارد نشده اید' , 'warning')
    return(redirect(url_for('admin.login')))




@admin.route('/list_users/' , methods=['GET'])
@admin_only_view
def list_users():
    users = User.query.order_by(User.id.desc()).all()
    return render_template('admin/list_users.html' , users=users)





@admin.route('/users/new/' , methods=['GET','POST'])
@admin_only_view
def create_user():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('admin/create_user.html', form=form)
        if not form.password.data == form.confirm_password.data:
            error_msg = 'Password and Confirm Password does not match.'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
            return render_template('admin/create_user.html', form=form)
        old_username = User.query.filter(User.username.ilike(form.username.data)).first()
        if old_username:
            flash('نام کاربری تکراری میباشد' , 'error')
            return render_template('admin/create_user.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('ایمیل تکراری می باشد' , 'error')
            return render_template('admin/create_user.html', form=form)

        

        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        new_user.phone_number = form.phone_number.data
        db.session.add(new_user)
        db.session.commit()
        
        flash('کاربر با موفقیت ساخته شد' , 'success')
        return redirect(url_for('admin.index'))
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('Email is in use.' , 'error')
    return render_template('admin/create_user.html', form=form)





# @admin.route('/projectss')
# @admin_only_view
# def projects():
#     projects = kh_project.query.order_by(kh_project.id.desc()).all()

#     return render_template('admin/projects.html' , projects=projects)



@admin.route('/<string:slug>')
@admin_only_view
def single_project(slug):
    project = kh_project.query.filter(kh_project.slug == slug).first_or_404()
    project_name = File.query.filter(File.project_name == project.project_name)



    return render_template('admin/single_project.html' , project=project , project_name=project_name)




@admin.route('/projects/' , methods=['GET'])
@admin_only_view
def list_projects():
    projects= kh_project.query.order_by(kh_project.id.desc()).all()
    return render_template('admin/list_projects.html' , projects=projects)




@admin.route('/projects/delete/<int:project_id>' , methods=['GET'])
@admin_only_view
def delete_project(project_id):
    project = kh_project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('پروژه حذف شد' , 'warning')
    return redirect(url_for('admin.list_projects'))





