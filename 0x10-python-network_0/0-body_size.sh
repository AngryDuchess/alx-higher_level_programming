#!/bin/bash
# Using curl to get the content-length of a url
curl -sI "$1" | wc -c
