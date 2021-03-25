#!/usr/bin/env python3

# See LICENSE.md for copyright and license details.

import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import Order, Product, Customer

app = create_app(os.getenv('FLASK_MODE', 'development'))
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Order=Order, Product=Product, Customer=Customer)

# @app.cli.command()
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=="__main__":
        app.run(debug=True)
