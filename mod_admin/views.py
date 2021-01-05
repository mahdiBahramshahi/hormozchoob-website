from flask import session , render_template , request , abort , flash , redirect, url_for
from mod_users.forms import LoginForm
from mod_users.models import User
from .import admin
from .utils import admin_only_view


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