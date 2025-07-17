#!/bin/bash
#catch errors
trap 'echo Received SIGTERM, finishing; exit' SIGTERM;
#run the main container service
#uvicorn main:app --reload --host 0.0.0.0 --port 8000
PYTHONPATH=./src uvicorn main:app --reload --host 0.0.0.0 --port 8000

