#!/bin/bash
# Retrieves the status code of request sent to given URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
