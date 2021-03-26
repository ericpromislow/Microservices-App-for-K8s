from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Customer

@api.route('/customers/')
def get_customers():
    page = request.args.get('page', 1, type=int)
    pagination = Customer.query.paginate(
        page, per_page=current_app.config['SOCKSESS_CUSTOMERS_PER_PAGE'],
        error_out=False)
    customers = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_customers', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_customers', page=page+1)
    return jsonify({
        'customers': [customer.to_json() for customer in customers],
        'prev': prev,
        'next': next,
        'count': pagination.total,
        'pages': pagination.pages,
    })

@api.route('/customers/<int:id>')
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_json())

@api.route('/customers/', methods=['CUSTOMER'])
def new_customer():
    customer = Customer.from_json(request.json)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json()), 201, \
        {'Location': url_for('api.get_customer', id=customer.id)}

@api.route('/customers/<int:id>', methods=['PUT'])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    customer.body = request.json.get('body', customer.body)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json())
