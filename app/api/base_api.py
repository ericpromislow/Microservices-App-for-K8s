import json

from flask import jsonify, request, current_app, url_for
from .. import db

def get_items(item_class, item_name, page_size_env_var):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', current_app.config[page_size_env_var], type=int)
    pagination = item_class.query.paginate(
        page,
        per_page=per_page,
        error_out=False)
    items = pagination.items
    urlname = 'api.get_' + item_name
    first = url_for(urlname, page=page-1)
    last = url_for(urlname, page=(--0--pagination.total//per_page))
    prev = pagination.has_prev and url_for(urlname, page=page-1) or None
    next = pagination.has_next and url_for(urlname, page=page+1) or None
    return jsonify({
        'resources': {
            item_name: [item.to_json() for item in items],
        },
        'pagination': {
            'first': first,
            'prev': prev,
            'next': next,
            'last': last,
            'count': pagination.total,
            'pages': pagination.pages,
        },
    })

def get_item(item_class, id):
    item = item_class.query.get_or_404(id)
    return jsonify(item.to_json())

import sys
def new_item(item_class, item_name):
    item = item_class.from_json(request.data)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_json()), 201, \
        {'Location': url_for('api.get_' + item_name, id=item.id)}

def edit_item(item_class, id):
    item = item_class.query.get_or_404(id)
    new_values = json.loads(request.data)
    for k, v in new_values.items():
        setattr(item, k, v)
    db.session.commit()
    return jsonify(item.to_json())

def delete_item(item_class, id):
    item = item_class.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return "{}", 204 
    
