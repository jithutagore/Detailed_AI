import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from .logging import new_request_id, request_id_var

logger = logging.getLogger("app.request")


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Assigns a request id (for log correlation) and logs method/path/status/duration."""

    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = new_request_id()
        token = request_id_var.set(request_id)
        started_at = time.perf_counter()
        try:
            response = await call_next(request)
        except Exception:
            logger.exception("%s %s failed", request.method, request.url.path)
            raise
        else:
            duration_ms = (time.perf_counter() - started_at) * 1000
            logger.info(
                "%s %s -> %d (%.1fms)",
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )
            response.headers["X-Request-ID"] = request_id
            return response
        finally:
            request_id_var.reset(token)
