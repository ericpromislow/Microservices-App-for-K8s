#!/usr/bin/env python3

# Usage: python3 load-data-from-json.py
#
# To reset the database:
# sqlite3: just delete the sqlite file and rerun this

import json
import os
import sys

from sqlalchemy import create_engine, insert, MetaData, text
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import DateTime, Float, Integer, String

#import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import app_config

def create_connection():
    print("QQQ: load-data-from-json.py: url: %s" % app_config.DB_URL, file=sys.stdout)
    url = app_config.DB_URL
    engine = create_engine(url)
    return engine

def create_tables(engine):
    metadata = MetaData()

    customer_table = Table(
        "customers",
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('first_name', String(64)),
        Column('last_name', String(64), nullable=False),
        Column('address', String(64), nullable=False),
        Column('city', String(64), nullable=False),
        Column('state', String(32)),
        Column('zip', String(32)),
        Column('country', String(4), nullable=False)
        )

    product_table = Table(
        "products",
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('code', String(32), nullable=False),
        Column('name', String(64), nullable=False),
        Column('description', String),
        Column('price', Float, nullable=False),
        Column('picture', String(256))
        )

    order_table = Table(
        "orders",
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('product_id', ForeignKey('products.id'), nullable=False),
        Column('customer_id', ForeignKey('customers.id'), nullable=False),
        Column('quantity', Integer),
        Column('price', Float),
        Column('timestamp', DateTime)
        )
    metadata.create_all(engine)
    conn = engine.connect()
    return (conn, customer_table, product_table, order_table)

def do_products(conn, product_table):
    with open("data/products.json") as fd:
        products = json.load(fd)['products']
    conn.execute(insert(product_table), products)

def do_customers(conn, customer_table):
    with open("data/customers.json") as fd:
        customers = json.load(fd)
    conn.execute(insert(customer_table), customers)

def main():
    engine = create_connection()
    conn, customer_table, product_table, order_table = create_tables(engine)
    do_products(conn, product_table)
    do_customers(conn, customer_table)
    #conn.commit() # Not an attribute -- ?
    conn.close()
        
if __name__ == '__main__':
    main()
