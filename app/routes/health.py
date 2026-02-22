from fastapi import APIRouter, Request
from datetime import datetime, timezone

router = APIRouter()


@router.get("/health", summary="Health Check")
async def health_check(request: Request):
    """
    Returns the current health status of the API.
    Use this endpoint to verify the server is running.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": request.app.version,
    }