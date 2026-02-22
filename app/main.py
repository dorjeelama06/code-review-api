from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.routes.review import router as review_router

from app.config import get_settings
from app.routes.health import router as health_router

settings = get_settings()

# Rate limiter
limiter = Limiter(key_func=get_remote_address, default_limits=[settings.rate_limit])

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="An AI-powered code review API that analyzes Git diffs and provides structured feedback.",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Attach rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Routers
app.include_router(health_router, tags=["Health"])
app.include_router(review_router, tags=["Review"])

@app.on_event("startup")
async def startup_event():
    print(f"🚀 {settings.app_name} v{settings.app_version} started")


@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Server shutting down")