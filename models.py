import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    buyer_id = db.Column(db.String(100))
    city = db.Column(db.String(100))

    def __repr__(self):
        return "<Order item:%r quantity:%d buyer:%r city:%r>" % (self.item, self.quantity, self.buyer_id, self.city)
