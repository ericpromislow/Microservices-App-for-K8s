#!/usr/bin/env python3

# Usage: python3 load-data-from-json.py
#
# To reset the database:
# sqlite3: just delete the sqlite file and rerun this

import json
import os
import sys
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import app_config

def create_connection():
    db_file = app_config.DB_URL.split("sqlite:///")
    path = db_file[0] or db_file[1]
    try:
        conn = sqlite3.connect(path)
    except:
        print("can't open file %s" % path)
        raise
    return conn

def create_tables(cur):
    cur.execute('''CREATE TABLE customers(id integer primary key autoincrement,
                   first_name string,
                   last_name string,
                   address string,
                   city string,
                   state string,
                   zip string,
                   country string)''')
    cur.execute('''CREATE TABLE products(id integer primary key autoincrement,
                      code string,
                      name string,
                      description string,
                      price real,
                      picture string)''')
    cur.execute('''CREATE TABLE orders(id integer primary key autoincrement,
                    customer_id integer,
                    product_id integer,
                    quantity integer,
                    price real,
                    timestamp integer)''')

def do_products(cur):
    with open("data/products.json") as fd:
        products = json.load(fd)['products']
    sql = '''INSERT into products(id, code, name, description, picture, price)
             VALUES(?, ?, ?, ?, ?, ?)'''
    for item in products:
        values = (item["id"], item["code"], item["name"], item["description"], item["picture"], item["price"])
        cur.execute(sql, values)

def do_customers(cur):
    with open("data/customers.json") as fd:
        customers = json.load(fd)
    sql = '''INSERT into customers(id, first_name, last_name, address, city, state, zip, country)
             VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
    for item in customers:
        values = (item["id"], item["first_name"], item["last_name"], item["address"],
                  item["city"], item["state"], item["zip"], item["country"])
        cur.execute(sql, values)

def main():
    conn = create_connection()
    cur = conn.cursor()
    create_tables(cur)
    do_products(cur)
    do_customers(cur)
    conn.commit()
    conn.close()
        
if __name__ == '__main__':
    main()
