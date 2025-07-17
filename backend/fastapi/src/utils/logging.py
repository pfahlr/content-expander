# src/utils/logging.py
import os
import sys
import logging
from rich.logging import RichHandler
from rich.traceback import install
LOG_LEVEL = os.getenv("LOG_LEVEL","INFO")

#def setup_logging(level: str = "INFO"):
if not logging.getLogger().hasHandlers():
  install(show_locals=True) 
  logging.basicConfig(
    level=LOG_LEVEL,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True,markup=True)]
  )
else: 
  log.error("Something is overriding our logger, and it is responsible for this message... so at least it works!")

log = logging.getLogger("content-expander")