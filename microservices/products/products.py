from flask import Flask, render_template
from flask import request, abort, url_for
import json
import html
from json2html import *


app = Flask(__name__)

# read file
with open('./data/products.json', 'r') as myfile:
    pro_data = myfile.read()

@app.route("/products")
def products():
    """Products page for web app"""
    pro_table = (json2html.convert(json = pro_data))
    return render_template("products.html", table_data=pro_table)
#    return render_template(
#            "products.html", title="page", jsonfile=json.dumps(data))


if __name__=="__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
