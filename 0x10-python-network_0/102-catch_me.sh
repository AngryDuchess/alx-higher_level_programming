#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me with curl
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
