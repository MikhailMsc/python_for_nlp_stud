from flask_app import db


class Anketa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120))
    age = db.Column(db.Integer)
    education = db.Column(db.String(200))
    languages = db.Column(db.String(200))
    comment = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Anketa from "{self.username}"/"{self.email}">'