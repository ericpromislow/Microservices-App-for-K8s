from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Order

@api.route('/orders/')
def get_orders():
    page = request.args.get('page', 1, type=int)
    pagination = Order.query.paginate(
        page, per_page=current_app.config['SOCKSESS_ORDERS_PER_PAGE'],
        error_out=False)
    orders = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_orders', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_orders', page=page+1)
    return jsonify({
        'orders': [order.to_json() for order in orders],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@api.route('/orders/<int:id>')
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_json())

@api.route('/orders/', methods=['ORDER'])
def new_order():
    order = Order.from_json(request.json)
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_json()), 201, \
        {'Location': url_for('api.get_order', id=order.id)}

@api.route('/orders/<int:id>', methods=['PUT'])
def edit_order(id):
    order = Order.query.get_or_404(id)
    order.body = request.json.get('body', order.body)
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_json())
