import json
import time
from datetime import datetime

from flask import current_app, url_for

from . import db

class ValidationError(ValueError):
    pass

class Customer(db.Model):
    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip = db.Column(db.String(16))
    country = db.Column(db.String(64))

    def to_json(self):
        jcust = {
            'id': self.id,
            'url': url_for('api.get_customer', id=self.id),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'country': self.country
            }
        return jcust

    @staticmethod
    def from_json(jcust):
        checker = {
            'first_name': True,
            'last_name': True,
            'address': True,
            'city': True,
            'state': True,
            'zip': False,
            'country': True,
            }
        packet = json.loads(jcust)
        for k, v in checker.items():
            if v and not (k in packet):
                raise ValidationError("customer does not have a %s field" % (k,))

        return Customer(first_name=packet['first_name'],
                        last_name=packet['last_name'],
                        address=packet['address'],
                        city=packet['city'],
                        state=packet['state'],
                        zip=packet['zip'],
                        country=packet['country'])

    def __repr__(self):
        return "<Customer id:%d name:%s %s>" % (self.id, self.first_name, self.last_name)

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32))
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    picture = db.Column(db.String(100))

    def to_json(self):
        jprod = {
            'id': self.id,
            'url': url_for('api.get_product', id=self.id),
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'picture': self.picture,
            }
        return jprod

    @staticmethod
    def from_json(payload):
        checker = {
            'code': True,
            'name': False,
            'description': True,
            'price': True,
            'picture': False,
            }
        dict = {}
        packet = json.loads(payload)
        for k, v in checker.items():
            if k in packet:
                dict[k] = packet[k]
            elif v:
                raise ValidationError("product does not have a %s field" % (k,))

        return Product(**dict)

    def __repr__(self):
        return "<Product id:%d name:%s cost:%2.2f>" % (self.id, self.name, self.price)
       
class Order(db.Model):
    __tablename__ = "orders"

    #extra = {}
    #if not 'sqlite' in current_app.config['SQLALCHEMY_DATABASE_URI']:
    #    extra['autocomplete'] = True
    #id = db.Column(db.Integer, primary_key=True, **extra)
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def to_json(self):
        jorder = {
            'id': self.id,
            'url': url_for('api.get_order', id=self.id),
            'customer_id': self.customer_id,
            'customer_url': url_for('api.get_customer', id=self.customer_id),
            'product_url': url_for('api.get_product', id=self.product_id),
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
            'timestamp': self.timestamp,
            }
        return jorder

    @staticmethod
    def from_json(jcust):
        checker = {
            'customer_id': True,
            'product_id': True,
            'quantity': False,
            'price': True,
            }
        packet = json.loads(jcust)
        for k, v in checker.items():
            if v and not (k in packet):
                raise ValidationError("order does not have a %s field" % (k,))
        quantity = packet['quantity'] or 1

        return Order(
            customer_id=packet['customer_id'],
            product_id=packet['product_id'],
            quantity=quantity,
            price=packet['price'],
            timestamp=datetime.fromtimestamp(time.time())
)

    def __repr__(self):
        return "<Order id:%d item:%r quantity:%d buyer:%r city:%r>" % (self.id, self.product_id, self.quantity, self.customer_id)
