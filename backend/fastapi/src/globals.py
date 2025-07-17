import os
from dotenv import load_dotenv
from pathlib import Path
from utils.logging import log

env_file = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=env_file)

log.info("Loading GLOBALS from: "+str(env_file))

WEBSITE_NAME = os.getenv("WEBSITE_NAME","[WEBSITE_NAME unset in /.env]")
log.info("WEBSITE_NAME: "+WEBSITE_NAME)

WEBSITE_EMAIL = os.getenv("WEBSITE_EMAIL","[WEBSITE_EMAIL unset in /.env]")
log.info("WEBSITE_EMAIL: "+WEBSITE_EMAIL)

WEBSITE_PHONE = os.getenv("WEBSITE_PHONE","[WEBSITE_PHONE unset in /.env]")
log.info("WEBSITE_PHONE: "+WEBSITE_PHONE)

DATABASE_URL = os.getenv("DATABASE_URL", "[DB_URL unset in /.env]")
log.info("DATABASE_URL: "+DATABASE_URL)

