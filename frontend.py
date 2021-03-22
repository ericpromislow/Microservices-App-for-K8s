from flask import Flask, render_template
from flask import request, url_for, flash, redirect
import json
import html
from json2html import *

from db_setup import init_db, db_session
from form import OrderForm
from models import Orders
#from models import db
#from . import config

app = Flask(__name__,template_folder='templates')

init_db()
#db.init(app)
#db.create_all()


# read file
with open('./data/products.json', 'r') as profile:
    pro_data = profile.read()

@app.route("/")
def home():
    """Home page for web app"""
    return render_template("home.html")

@app.route("/products", methods=['GET'])
def products():
    """Products page for web app"""
    pro_table = (json2html.convert(json = pro_data))
    return render_template("products.html", table_data=pro_table)
#    return render_template(
#            "products.html", title="page", jsonfile=json.dumps(data))

@app.route("/orders", methods=['GET', 'POST'])
def orders():
    """ Add a new Order"""
    form = OrderForm(request.form)
#    if request.method == 'POST' and form.validate():
    order = Orders()
    save_orders(order, form, new=True)
    flash('Order placed successfully')
    return redirect("/")
    return render_template("orders.html", form=form)

def save_orders(order, form, new=True):
    """Save orders to database"""
# how to write data to a db

    item = Orders()
    item.name = form.item.data

    order.item = form.item.data
    order.quantity = form.quantity.data
    order.buyer_id = form.buyer_id.data
    order.city = form.city.data
    db_session.add(order)
    db_session.commit()



if __name__=="__main__":
        app.run(debug=True)
