# src/utils/logging.py
import logging
from rich.logging import RichHandler
from rich.traceback import install


def setup_logging(level: str = "INFO") -> None:
  if not logging.getLogger().hasHandlers():
    install(show_locals=True) 
    logging.basicConfig(
      level=level,
      format="%(message)s",
      datefmt="[%X]",
      handlers=[RichHandler(rich_tracebacks=True,markup=True)]
    )
  else: 
    log.error("Something is overriding our logger, and it is responsible for this message... so at least it works!")
