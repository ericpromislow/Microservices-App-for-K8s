#!/bin/bash

# postgres:
export SOCKSESS_DB=postgresql+psycopg2://socksess:socksess@127.0.0.1:5432/socksess

# sqlite:
# export SOCKSESS_DB=sqlite+pysqlite:///$(dirname $(dirname $(realpath "$0")))/myorders.db
export FLASK_APP=frontend.py
export FLASK_DEBUG=1
flask run
