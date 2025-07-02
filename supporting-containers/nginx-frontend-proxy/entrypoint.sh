#!/bin/bash
#catch errors
trap 'echo Received SIGTERM, finishing; exit' SIGTERM;
#run the main container service
nginx -g daemon off 
