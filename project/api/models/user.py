from sqlalchemy.orm import defaultload
from .database import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from ..start import app
import time

class User(db.Model):
    DEFAULT_PARENT = 1
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    parent = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    #affiliates = db.relationship('User', backref='parent', lazy=True)
    role = db.relationship('Role', uselist=False)

    def __init__(self, email=None, password=None, telephone=None, role_id=None, parent=DEFAULT_PARENT):
        self.email = email
        self.password = password
        self.telephone = telephone
        self.role_id = role_id
        self.parent = parent
        
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id'])