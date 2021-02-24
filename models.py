# from flask import Flask
# from marshmallow import Schema, fields, pre_load, validate
# from flask_marshmallow import Marshmallow
# from flask_sqlalchemy import SQLAlchemy
from proyecto_inventario import db


def load_store(store_id):
    return Store.query.get(int(store_id))


class Store(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=True)
    address = db.Column(db.String(120), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    products = db.relationship('Product', backref='storesname', lazy=True)

    def __init__(self, name, address, description, email):
        self.name = name
        self.description = description
        self.address = address
        self.email = email


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text, nullable=True)
    sku = db.Column(db.Integer)
    image = db.Column(db.String(150), nullable=True, default='no-image.jpg')
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    def __init__(self, name, description, sku, price, quantity, store_id):
        self.name = name
        self.description = description
        self.sku = sku
        self.price = price
        self.quantity = quantity
        self.store_id = store_id


