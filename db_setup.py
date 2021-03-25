import os
import sys

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

import config
from models import Customer

def init_db(app):
    db_url = config.config.SQLALCHEMY_DATABASE_URI
    #print("QQQ: init_db: url: %s" % db_url, file=sys.stdout)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.config.SQLALCHEMY_TRACK_MODIFICATIONS
    db = SQLAlchemy(app)
    return db
