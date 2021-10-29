from datetime import datetime

from index import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(200), unique=True, index=True)
    password_hash = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "<User {}>".format(self.username)


class Product():
    pass
