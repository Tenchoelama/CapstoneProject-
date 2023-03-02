from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime, date


#Adding Flask security for passwords
from werkzeug.security import generate_password_hash

#Import secrets to generate user token 
import secrets

#flask login to check for an authentication user
from flask_login import UserMixin, LoginManager

#import for flask marshmallow
from flask_marshmallow import Marshmallow

#create instance of SQLAlchemy
db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model, UserMixin):
    #defining the coloumns of the User Table
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    quiz = db.relationship('QuizResult', backref='', lazy=True)
    
    #defining the constructor of the User Class
    def __init__(self, email, password, first_name = '', last_name = '', id = '',  token = ''):
        self.id = self.set_id()
        self.password = self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.token = self.set_token(24)
        
        
    #method for generating a unique id for the user
    def set_id(self):
        return str(uuid.uuid4())
    #method for generating a unique token for the user
    def set_token(self, length):
        return secrets.token_hex(length)
    #method for hasing the user's password
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    #method for representing the User Object as a string 
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    
    

class QuizResult(db.Model):
    id = db.Column(db.String, primary_key=True)
    quiz_name = db.Column(db.String(150), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    attempts = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.Date)
    
    
    def __init__(self, user_id, quiz_name='LOTR Quiz', score=0, attempts=0 ):
        self.id = self.set_id()
        self.quiz_name = quiz_name
        self.score = score
        self.attempts = attempts 
        self.user_id = user_id
        self.timestamp = date.today()
        
    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f"QuizAttempt {self.id} - Quiz: {self.quiz_name}, Score: {self.score}, Attempts: {self.attempts}"
    