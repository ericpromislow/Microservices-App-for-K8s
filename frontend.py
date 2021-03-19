from flask import Flask, render_template
from flask import request, url_for, flash, redirect
import json
import html
from json2html import *

from orderform import OrderForm


app = Flask(__name__,template_folder='templates')

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

@app.route("/orders")
def orders():
    """ Add a new Order"""
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        order = Orders()
        save_orders(order, form, new=True)
        flash('Order placed successfully')
        return redirect("/")
    return render_template("orders.html", form=form)

def save_orders(new_order, form, new=False):
    """Save orders to database"""
# how to write data to a db


if __name__=="__main__":
    app.run(debug=True)
