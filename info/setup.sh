# Assume using python3

# venv - comes with python3 -- not using it for this project anyway

pip3 install json2html

pip3 install flask
pip3 install flask_sqlalchemy

pip3 install flask-bootstrap
pip3 install flask-wtf

pip3 install Faker


DATABASE:
# Creating the database

CREATE TABLE customers(id integer primary key autoincrement,
                       first_name string,
                       last_name string,
                       address string,
                       city string,
                       state string,
                       zip string,
                       country string);

CREATE TABLE products(id integer primary key autoincrement,
                      code string,
                      name string,
                      description string,
                      price real
                      picture string);

CREATE TABLE orders(id integer primary key autoincrement,
                    customer_id integer,
                    product_id integer,
                    quantity integer,
                    price real,
                    timestamp integer);

# Adding the data
python3 scripts/populate-customer-table.py
python3 scripts/load-data-from-json.py


