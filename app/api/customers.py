from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Customer

from . import base_api

@api.route('/customers/')
def get_customers():
    return base_api.get_items(Customer, 'customers', 'SOCKSESS_CUSTOMERS_PER_PAGE')

@api.route('/customers/<int:id>')
def get_customer(id):
    return base_api.get_item(Customer, id)

@api.route('/customers/', methods=['POST'])
def new_customer():
    return base_api.new_item(Customer, 'customer')

@api.route('/customers/<int:id>', methods=['PUT'])
def edit_customer(id):
    return base_api.edit_item(Customer, id)

@api.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    return base_api.delete_item(Customer, id)
