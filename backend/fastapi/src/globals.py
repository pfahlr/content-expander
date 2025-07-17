import os
from dotenv import load_dotenv
from pathlib import Path
from utils.logging import log

### ---------------     ACCESS FILE SYSTEM PATH HIERARCHY     ------------- ###

#[repo_root]]/
PROJECT_ROOT=Path(__file__).resolve().parents[3]
#[repo_root]/backend/
PROJECT_BACKEND_ROOT=Path(__file__).resolve().parents[2]
#[repo_root]/backend/fastapi/
PROJECT_BACKEND_FASTAPI_ROOT=Path(__file__).resolve().parents[1]
#[repo root]/backend/fastapi/src/
PROJECT_BACKEND_FASTAPI_SRC_ROOT=Path(__file__).resolve().parents[0]
#[repo root]/backend/fastapi/src/.env
ENV_FILE = PROJECT_ROOT / ".env"

env_file=ENV_FILE

load_dotenv(dotenv_path=env_file)

### ----- LOAD GLOBAL CONFIGURATION VALUES (ENVIRONMENT VARIABLES)   ------ ###

log.info("Loading GLOBALS from: "+str(env_file))

WEBSITE_NAME = os.getenv("WEBSITE_NAME","[WEBSITE_NAME unset in /.env]")
log.info("WEBSITE_NAME: "+WEBSITE_NAME)

WEBSITE_EMAIL = os.getenv("WEBSITE_EMAIL","[WEBSITE_EMAIL unset in /.env]")
log.info("WEBSITE_EMAIL: "+WEBSITE_EMAIL)

WEBSITE_PHONE = os.getenv("WEBSITE_PHONE","[WEBSITE_PHONE unset in /.env]")
log.info("WEBSITE_PHONE: "+WEBSITE_PHONE)

DATABASE_URL = os.getenv("DATABASE_URL", "[DATABASE_URL unset in /.env]")
log.info("DATABASE_URL: "+DATABASE_URL)

ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL", "[ASYNC_DATABASE_URL unset in /.env]")
log.info("ASYNC_DATABASE_URL: "+ASYNC_DATABASE_URL)

FASTAPI_USERS_SECRET = os.getenv("FASTAPI_USERS_SECRET", "[FASTAPI_USERS_SECRET unset in /.env]")
log.info("FASTAPI_USERS_SECRET: "+FASTAPI_USERS_SECRET)

FASTAPI_USERS_PRIVATE_KEY = os.getenv("FASTAPI_USERS_PRIVATE_KEY", "[FASTAPI_USERS_PRIVATE_KEY unset in /.env]")
log.info("FASTAPI_USERS_PRIVATE_KEY: "+FASTAPI_USERS_PRIVATE_KEY)

FASTAPI_USERS_PUBLIC_KEY = os.getenv("FASTAPI_USERS_PUBLIC_KEY", "[FASTAPI_USERS_PUBLIC_KEY unset in /.env]")
log.info("FASTAPI_USERS_PUBLIC_KEY: "+FASTAPI_USERS_PUBLIC_KEY)

FASTAPI_KEYPAIR_ALGO = os.getenv("FASTAPI_KEYPAIR_ALGO", "[FASTAPI_KEYPAIR_ALGO unset in /.env]")
log.info("FASTAPI_KEYPAIR_ALGO: "+FASTAPI_KEYPAIR_ALGO)

### ----------------------------------------------------------------------- ###

