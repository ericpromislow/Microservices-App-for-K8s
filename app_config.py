import secrets
import os

basedir = os.path.abspath(os.path.dirname(__file__))

import sys
sys.stderr.write("basedir: %s\n" % (basedir,))

SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_hex(32))
DB_URL = os.environ.get("SOCKSESS_DB", 'sqlite:///' + os.path.join(basedir, 'myorders.db'))
