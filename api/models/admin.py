from .database import db 

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __init__(self, firstname, lastname, user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.user_id = user_id