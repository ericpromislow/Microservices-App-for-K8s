from flask import Flask, render_template
from flask import request, abort, url_for
import json
import html

app = Flask(__name__,template_folder='')

# read file
with open('./data/orders.json', 'r') as myfile:
    data = myfile.read()

@app.route("/orders")
def orders():
    return render_template("orders.html")


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port='5002')
