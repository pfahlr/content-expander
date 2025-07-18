#!/bin/sh
#catch errors
trap 'echo Received SIGTERM, finishing; exit' SIGTERM;
cd content-expander-frontend
npm run dev --  --host  --port 5173
