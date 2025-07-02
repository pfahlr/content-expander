#!/bin/sh
container_status_placeholder=True
container_ok=container_status_placeholder

if [[ container_ok ]]; then 
  #echo "container ok!"
  exit 0
else
  #echo "container not ok :("
  exit 1
fi
