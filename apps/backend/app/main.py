import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine

from app.api.router import api_router, router
from app.core.config import settings
from app.infrastructure.database.config import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создание таблиц в базе данных
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    if isinstance(engine, AsyncEngine):
        await engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

router.include_router(api_router)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    # Run application
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
