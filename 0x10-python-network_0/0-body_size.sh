#!/bin/bash
# Using curl to get the content-length of a url
echo curl -sI "$1" | wc -c
