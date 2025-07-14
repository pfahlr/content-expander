POSTGRES_USER=webcontmgr
POSTGRES_HOST=webcontmgr-db
POSTGRES_DB=webcontmgr
POSTGRES_PASSWORD= ---[REDACTED]---
POSTGRES_PORT=5432
# local development
POSTGRES_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5433/${POSTGRES_DB}"
# containerized development 
POSTGRES_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
DATABASE_URL=$POSTGRES_URL

#POSTGRES_URL="postgresql://symfony:symfony@db:5432/symfony?serverVersion=16"
#DATABASE_URL="postgresql://symfony:symfony@db:5432/symfony?serverVersion=16"

OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o


