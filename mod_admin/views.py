from flask import session , render_template , request , abort , flash , redirect, url_for
from mod_users.forms import LoginForm
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
            flash("Incorrect credentials", category='error')
            return render_template('admin/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("Incorrect credentials", category='error')
            return render_template('admin/login.html', form=form)

        if not user.is_admin():
            flash("Incorrect credentials", category='error')
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

@admin.route('/projectss')
@admin_only_view
def projects():
    projects = kh_project.query.order_by(kh_project.id.desc()).all()

    return render_template('admin/projects.html' , projects=projects)

@admin.route('/<string:slug>')
@admin_only_view
def single_project(slug):
    project = kh_project.query.filter(kh_project.slug == slug).first_or_404()
    project_name = File.query.filter(File.project_name == project.project_name)



    return render_template('admin/single_project.html' , project=project , project_name=project_name)




@admin.route('/projects' , methods=['GET'])
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





