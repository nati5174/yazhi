import asyncio
from .database import engine, Base
from .model import PrMetadata  # Import models so they register with Base.metadata

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_db())
