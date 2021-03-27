from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Product

from . import base_api

@api.route('/products/')
def get_products():
    return base_api.get_items(Product, 'products', 'SOCKSESS_PRODUCTS_PER_PAGE')

@api.route('/products/<int:id>')
def get_product(id):
    return base_api.get_item(Product, id)

@api.route('/products/', methods=['POST'])
def new_product():
    return base_api.new_item(Product, 'product')

@api.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    return base_api.edit_item(Product, id)

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    return base_api.delete_item(Product, id)

