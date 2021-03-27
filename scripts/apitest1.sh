#!/bin/bash

# New product:

curl -H "Content-type: text/json" -X POST http://127.0.0.1:5000/api/v1/products/  -d '{"name":"cones", "description":"pictures of cones", "price":12.99, "code":"some code"}'

# New customer:

curl -H "Content-type: text/json" -X POST http://127.0.0.1:5000/api/v1/customers/  -d '{"first_name":"John", "last_name":"Smithers", "address":"10 Milltown Road", "city":"Boston","state":"MA", "zip":"02134", "country":"US"}'

# New order:
curl -H "Content-type: text/json" -X POST http://127.0.0.1:5000/api/v1/orders/  -d '{"customer_id":4, "product_id":2, "quantity": 10, "price":9.89}'

Fix the product
curl -H "Content-type: text/json" -X PUT http://127.0.0.1:5000/api/v1/products/8  -d '{"code":4, "PRO-SOCKS-008"}'




