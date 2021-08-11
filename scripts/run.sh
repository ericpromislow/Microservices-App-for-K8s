#!/bin/bash

# Let the database come up in a minute...
sleep 60

set -ex

flask db upgrade

set +e

flask run --host=0.0.0.0
