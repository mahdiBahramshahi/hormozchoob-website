from flask import request , render_template , flash , session , abort , redirect , url_for
from .models import User 
from app import db
from .forms import RegisterForm , LoginForm


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
        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('ایمیل تکراری می باشد' , 'error')
            return render_template('users/register.html', form=form)
        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
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
            flash("نام کابری / رمز ورود  نادرست است", category='error')
            return render_template('users/login.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='error')
        #     return(redirect(url_for('index')))
        
        session['email'] = user.email
        session['user_id'] = user.id

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