#!/usr/bin/env python3

# See LICENSE.md for copyright and license details.

from flask import Flask, render_template
from flask import request, url_for, flash, redirect

from flask_bootstrap import Bootstrap

import json
from json2html import json2html
import html
import re
import sys
import time
import datetime

import app_config
import db_setup
from forms.orders.add import OrderForm
from models import Order, Product, Customer

print("QQQ: Hey we're doing an app!")

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = app_config.SECRET_KEY

db = db_setup.init_db(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    """Home page for web app"""
    return render_template("home.html")

@app.route("/products", methods=['GET'])
def products():
    """Products page for web app"""
    products = Product.query.all()
    return render_template("products.html", products=products)

@app.route("/order_form", methods=['GET', 'POST'])
def order_form():
    if request.method == "GET":
        form = OrderForm()
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

class OrderForView(object):
    def __init__(self, order):
        customer = Customer.query.filter_by(id=order.customer_id)[0]
        product = Product.query.filter_by(id=order.product_id)[0]

        self.product_name = product.name
        self.quantity = order.quantity
        self.total_cost = order.quantity * order.price
        self.customer_name = "%s %s" % (customer.first_name, customer.last_name)
        self.date_ordered = order.timestamp.ctime()

@app.route("/orders", methods=['GET'])
def orders():
    # Keep business logic here -- convert the database Order into a class
    # better suited for displaying data
    current_orders = [OrderForView(order) for order in Order.query.all()]
    return render_template("orders.html", orders=current_orders)

@app.route("/customers", methods=['GET'])
def customers():
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

def save_orders(form):
    """Save orders to database"""
    order = Order()

    item_name = form.item.data
    product = Product.query.filter_by(name=item_name)[0]

    names = re.split(" ", form.buyer.data, 1)
    customer = Customer.query.filter_by(first_name=names[0], last_name=names[1])[0]

    order.product_id = product.id
    order.customer_id = customer.id
    order.quantity = form.quantity.data
    order.price = product.price
    order.timestamp = datetime.datetime.fromtimestamp(time.time())

    db.session.add(order)
    db.session.commit()



if __name__=="__main__":
        app.run(debug=True)
