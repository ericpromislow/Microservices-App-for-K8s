import os
import sys

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

import app_config
from models import Customer

def init_db(app):
    print("QQQ: init_db: url: %s" % app_config.DB_URL, file=sys.stdout)
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    try:
        print("QQQ: %d - %d" % (Customer.query.count(), Product.query.count()))
    except:
        os.system("python3 scripts/load-data-from-json.py")
    return db
