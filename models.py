import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Orders(db.Model):
    __tablename__ = "orders"
    column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    buyer_id = db.Column(db.String(100))
    city = db.Column(db.String(100))