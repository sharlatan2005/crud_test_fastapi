from core.config import database_config
from collections.abc import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine(database_config.db_url, echo=True, pool_pre_ping=True)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_factory() as session, session.begin():
        yield session

async def close_database() -> None:
    await engine.dispose()