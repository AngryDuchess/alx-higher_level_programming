#!/bin/bash
# using curl to get the value stored in a header variable
curl -sH "X-School-User-Id:98" "$1"
