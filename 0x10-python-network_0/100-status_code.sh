#!/bin/bash
# prints out the http status code of a url passed
curl -s -o /dev/null -w "%{http_code}" "$1"
