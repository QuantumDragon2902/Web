from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy(user.db)


class User(db.Model, UserMixin):
    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.login