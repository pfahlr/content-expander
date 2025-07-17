from globals import DATABASE_URL, log
#import os
#import sys
#from pathlib import Path
#from dotenv import load_dotenv
from sqlmodel import create_engine, Session

#ATABASE_URL = os.getenv("DATABASE_URL")
#log.info(DATABASE_URL)
# Create the shared engine
log.info('opening database connection')
engine = create_engine(DATABASE_URL, echo=True)
log.info(engine)
# Optional session generator

def get_session():
    with Session(engine) as session:
        yield session