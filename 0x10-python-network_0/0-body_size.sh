#!/bin/bash
# Using curl to get the content-length of a url
curl -s "$1" | wc -c
