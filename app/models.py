from . import db

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

    def __repr__(self):
        return "<Product id:%d name:%s cost:%2.2f>" % (self.id, self.name, self.price)
       

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return "<Order id:%d item:%r quantity:%d buyer:%r city:%r>" % (self.id, self.product_id, self.quantity, self.customer_id)
