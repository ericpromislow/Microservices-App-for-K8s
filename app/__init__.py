from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    print("config_name:%s" % (config_name,))
    config_class = config[config_name]
    print("SQLALCHEMY_DATABASE_URI: %s" % (config_class.SQLALCHEMY_DATABASE_URI))
    app.config.from_object(config_class)

    print("dburl: %s" % (app.config['SQLALCHEMY_DATABASE_URI']))
    config_class.init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    # TODO: attach routes and error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app
