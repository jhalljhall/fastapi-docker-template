#!/bin/bash
service postgresql start
# Add any other services you want to start, e.g., your application server

# Keep the container running
tail -f /dev/null
