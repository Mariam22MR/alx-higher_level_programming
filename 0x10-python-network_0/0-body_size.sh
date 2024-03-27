#!/bin/bash
# Gets the size of body of response from URL
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
