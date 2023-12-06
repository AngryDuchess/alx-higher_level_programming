#!/bin/bash
# sends a JSON post to a url
curl -s -H "Content-Type: application/json" -X POST -d "@$2" "$1"
