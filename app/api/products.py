from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Product

@api.route('/products/')
def get_products():
    page = request.args.get('page', 1, type=int)
    pagination = Product.query.paginate(
        page, per_page=current_app.config['SOCKSESS_PRODUCTS_PER_PAGE'],
        error_out=False)
    products = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_products', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_products', page=page+1)
    return jsonify({
        'products': [product.to_json() for product in products],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@api.route('/products/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_json())

@api.route('/products/', methods=['PRODUCT'])
def new_product():
    product = Product.from_json(request.json)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_json()), 201, \
        {'Location': url_for('api.get_product', id=product.id)}

@api.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    product = Product.query.get_or_404(id)
    product.body = request.json.get('body', product.body)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_json())
