
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

import app_config

# import models

# engine = create_engine(app_config.DB_URL, convert_unicode=True)

# db_session = scoped_session(sessionmaker(autocommit=False,
#                                         autoflush=False,
#                                         bind=engine))
# Base = declarative_base()
#Base.query = db_session.query_property()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db
