from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    binomial = db.Column(db.String(256), index=True, unique=True)
    description = db.Column(db.Text)
    identification = db.Column(db.Text)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.relationship('Image', backref='species', lazy='dynamic')

    def __repr__(self):
        return '<Species {}>'.format(self.binomial)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(256))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Image {}>'.format(self.species_id)


# Column(ARRAY(TEXT)) -- store a bunch of versions of the description

