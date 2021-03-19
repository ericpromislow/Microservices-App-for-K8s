from flask import Flask, render_template
from flask import request, abort, url_for
import json
import html

app = Flask(__name__,template_folder='templates')

# read file
with open('./data/products.json', 'r') as myfile:
    data = myfile.read()

@app.route("/products")
def products():
    return render_template(
            "products.html", title="page", jsonfile=json.dumps(data))


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port='5001')
