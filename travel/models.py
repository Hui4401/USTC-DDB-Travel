from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from travel.extensions import db


class User(db.Model, UserMixin):
    username = db.Column(db.String(64), primary_key=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_addr = db.Column(db.String(64))
    to_addr = db.Column(db.String(64))
    total_sites = db.Column(db.Integer)
    avail_sites = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Car(db.Model):
    location = db.Column(db.String(64), primary_key=True)
    car_type = db.Column(db.String(64), primary_key=True)
    total_cars = db.Column(db.Integer)
    avail_cars = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Hotel(db.Model):
    location = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), primary_key=True)
    total_rooms = db.Column(db.Integer)
    avail_rooms = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Reservation(db.Model):
    username = db.Column(db.String(64), primary_key=True)
    res_type = db.Column(db.String(64), primary_key=True)
    res_id = db.Column(db.Integer, primary_key=True)
    res_time = db.Column(db.DateTime, default=datetime.utcnow)


class ResFlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    flight_id = db.Column(db.Integer)


class ResCar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    car_location = db.Column(db.String(64))
    car_type = db.Column(db.String(64))


class ResHotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    hotel_location = db.Column(db.String(64))
    hotel_name = db.Column(db.String(64))
