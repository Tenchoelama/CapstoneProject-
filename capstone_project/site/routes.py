from flask import Blueprint, render_template
from flask_login import login_user,logout_user, login_required,current_user
from capstone_project.models import User, db, QuizResult





site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template("index.html")


@site.route('/profile')
@login_required
def profile():
    user = current_user
    first_name = user.first_name
    last_name = user.last_name
    quiz_results = QuizResult.query.filter_by(user_id=current_user.id).all()
    return render_template("profile.html", first_name=first_name, last_name=last_name, quiz_results=quiz_results)


@site.route('/tutor')
def tutor():
    return render_template('tutor.html')