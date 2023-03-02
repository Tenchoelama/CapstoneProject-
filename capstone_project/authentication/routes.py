
from flask import Blueprint, render_template, request, flash, redirect, url_for
from capstone_project.models import User, db
from capstone_project.forms import UserLoginForm, UserSignUpForm, ChangePassword
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user,logout_user, login_required
from flask_login import login_required, current_user



auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserSignUpForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data
            password1 = form.password1.data
            if password != password1:
                flash('Passwords do not match', 'error')
                return render_template('signup.html', form=form)
            user = User(email, password, first_name, last_name)
            
            db.session.add(user)
            db.session.commit()
            
            flash(f"You have successfully created a User account {email}", "user-created")
            
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid From Data: Please Check Your Form')
            
    return render_template('signup.html', form=form)
            
            
    

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully logged in via Email/Password', 'auth-success')
                return redirect(url_for('site.profile'))
    except:
        raise Exception("Invalid Form Data: Please check your form and try again")
    
    return render_template('signin.html', form=form)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))



@auth.route('/passwords', methods = ['GET','POST'])
@login_required
def change_password():
    form = ChangePassword()
    # if request.method == 'POST':
    return render_template('changepass.html', form=form)


@auth.route('/password', methods = ['PUT','POST'])
@login_required
def change_pass():
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    if new_password != confirm_password:
        flash('New passwords do not match')
        return redirect(url_for('auth.password'))

    current_user.password = generate_password_hash(new_password)
    db.session.commit()

    flash('Password changed successfully')
    return redirect(url_for('auth.signin'))

