#!/usr/bin/env python3

# See LICENSE.md for copyright and license details.

from flask import Flask, render_template
from flask import request, url_for, flash, redirect

from flask_bootstrap import Bootstrap

import json
from json2html import json2html
import html
import sys

import app_config
import db_setup
from forms.orders.add import OrderForm
from models import Order
#from models import db
#from . import config

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = app_config.SECRET_KEY

db = db_setup.init_db(app)
#db.init(app)
#db.create_all()


# read file
with open('./data/products.json', 'r') as profile:
    pro_data = profile.read()

@app.route("/", methods=['GET', 'POST'])
def index():
    """Home page for web app"""
    return render_template("home.html")

@app.route("/products", methods=['GET'])
def products():
    """Products page for web app"""
    #pro_table = (json2html.convert(json = pro_data))
    products=json.loads(pro_data)['products']
    sys.stderr.write("Hey products:\n")
    sys.stderr.write(repr(products))
    return render_template("products.html", products=products)
#    return render_template(
#            "products.html", title="page", jsonfile=json.dumps(data))

@app.route("/order_form", methods=['GET', 'POST'])
def order_form():
    if request.method == "GET":
        form = OrderForm() # ??? request.form)
        form.quantity.data = 1
        return render_template("order_form.html", form=form)
    form = OrderForm(request.form)
    if form.validate_on_submit():
        save_orders(form)
        flash('Order placed successfully')
        return redirect("/")
    else:
        flash('Order not valid')
        return render_template("order_form.html", form=form)

@app.route("/orders", methods=['GET'])
def orders():
    current_orders = Order.query.all()
    return render_template("orders.html", orders=current_orders)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

def save_orders(form):
    """Save orders to database"""
    order = Order()

    order.item = form.item.data
    order.quantity = form.quantity.data
    order.buyer_id = form.buyer_id.data
    order.city = form.city.data
    db.session.add(order)
    db.session.commit()



if __name__=="__main__":
        app.run(debug=True)
