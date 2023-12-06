#!/bin/bash
# sends a JSON post to a url
curl -sH "Content-Type: application/json" -X POST -d "@$2" "$1"
