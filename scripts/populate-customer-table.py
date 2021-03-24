#!/usr/bin/env python3

# To run: python3 populate-user-table [-n NUM=100] [JSONFILE]

import json
import os
import re
import sys

from faker import Faker
from faker.providers import person

fake =  Faker()
fake.add_provider(person)

n = 100
outfile = None

def usage(msg=None):
    if msg:
        print(msg, file=sys.stderr)
    print("Usage: %s [-n NUM] [OUTFILE | stdout]" % sys.argv[0], file=sys.stderr)
    sys.exit(1)    

idx = 1
while idx < len(sys.argv):
    if sys.argv[idx] == '-n':
        if idx == len(sys.argv) - 1:
            usage("missing size")
        n = int(sys.argv[idx + 1])
        idx += 1
    elif sys.argv[idx] == '-h':
        usage()
    elif sys.argv[idx][0] == '-':
        usage("Unexpected arg: %s" % sys.argv[idx])
    else:
        outfile = sys.argv[idx]
    idx += 1    

ptn = re.compile(r'(.+?)\s*\n(.+?),\s*(\w\w)\s+(\d+)')

def get_address():
    # Try 10 times -- we want to ignore APO/FPO/DPO box office and contact things
    for i in range(10):
        full_address = fake.address()
        m = ptn.match(full_address)
        if m:
            return m.groups()
        print("Couldn't address-match <%s> -- retrying" % full_address, file=sys.stderr)
    
data = []
for i in range(n):
    first_name = fake.first_name()
    last_name = fake.last_name()
    address, city, state, zip = get_address()
    data.append({'id': i + 1,
                 'first_name': first_name,
                 'last_name': last_name,
                 'address': address,
                 'city': city,
                 'state': state,
                 'zip': zip,
                 'country': 'US'})

fd = (outfile and open(outfile, 'w')) or sys.stdout

json.dump(data, fd, indent=2, ensure_ascii=True)
