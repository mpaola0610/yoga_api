from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
import flask_sqlalchemy
# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash
# Import Secrets
import secrets
#Imports for Login Manager
from flask_login import UserMixin
# Imports for Flask Login
from flask_login import LoginManager
# Immports Marsh..
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default='')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable=True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default= '', unique = True)
    date_created =  db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    sequence=  db.relationship('Sequence', backref = 'owner', lazy = True)
    
    def __init__(self, email, first_name= '', last_name= '', id = '', password= '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name= last_name
        self.password = self.set_password(password)
        self.email= email
        self.token = self.set_token(24)
        self.g_auth_verify= g_auth_verify
    
    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been added to the database.'

class Sequence(db.Model):
    id = db.Column(db.String, primary_key = True)
    warmups= db.Column(db.String(300), nullable = False)
    warriors = db.Column(db.String(300), nullable = False)
    balance = db.Column(db.String(300), nullable = False)
    cooldown = db.Column(db.String(300), nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self,warmups,warriors,balance,cooldown,user_token, id=''):
        self.id = self.set_id()
        self.warmups = warmups
        self.warriors = warriors
        self.balance = balance
        self.cooldown = cooldown
        self.user_token = user_token
    
    def __repr__(self):
        return f'Sequence has been added'

    def set_id(self):
        return secrets.token_urlsafe()

class SequenceSchema(ma.Schema):
    class Meta:
        fields = ['id','warmups','warriors','balance','cooldown']

sequence_schema = SequenceSchema()

sequences_schema = SequenceSchema(many = True)


