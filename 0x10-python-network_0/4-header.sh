#!/bin/bash
# Script that takes in a URL as an arg, sends a GET request to the URL, and displays the body
curl -s -H "X-School-User-Id:98" "$1"
