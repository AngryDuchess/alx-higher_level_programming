#!/bin/bash
# using curl to post data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
