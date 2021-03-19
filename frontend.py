from flask import Flask, render_template
from flask import request, url_for
import json
import html
from json2html import *

app = Flask(__name__,template_folder='templates')

# read files
with open('./data/products.json', 'r') as profile:
    pro_data = profile.read()

with open('./data/orders.json', 'r') as ordfile:
    ord_data = ordfile.read()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products", methods=['GET'])
def products():
    pro_table = (json2html.convert(json = pro_data))
    return render_template("products.html", table_data=pro_table)
#    return render_template(
#            "products.html", title="page", jsonfile=json.dumps(data))

@app.route("/orders")
def orders():
    ord_table = (json2html.convert(json = ord_data))
    return render_template("orders.html", table_data=ord_table)


if __name__=="__main__":
    app.run(debug=True)
