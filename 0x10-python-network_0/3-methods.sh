#!/bin/bash
# using curl to display all hhtp methods allowed
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
