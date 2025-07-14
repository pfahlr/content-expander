# src/middleware/log_requests.py
import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("fastapi")

class LogRequestMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    start_time = time.time()

    response: Response = await call_next(request)

    duration = time.time() - start_time
    log_msg = (
      f"{request.method} {request.url.path} "
      f"→ {response.status_code} ({duration:.2f}s)"
    )

    logger.info(log_msg)
    return response

