from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Order

from . import base_api

@api.route('/orders/')
def get_orders():
    return base_api.get_items(Order, 'orders', 'SOCKSESS_ORDERS_PER_PAGE')

@api.route('/orders/<int:id>')
def get_order(id):
    return base_api.get_item(Order, id)

@api.route('/orders/', methods=['POST'])
def new_order():
    return base_api.new_item(Order, 'order')

@api.route('/orders/<int:id>', methods=['PUT'])
def edit_order(id):
    return base_api.edit_item(Order, id)

@api.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    return base_api.delete_item(Order, id)
