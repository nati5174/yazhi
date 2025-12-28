from .model import PrMetadata
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

async def store_pull_request(ctx: Dict[str, Any], db: AsyncSession) -> dict:

    pr = PrMetadata( pr_number=ctx["pr_number"], 
                     repo_name=ctx["repo_name"], 
                     sha=ctx["sha"],
                     action=ctx["action"])

    db.add(pr)
    await db.commit()
    await db.refresh(pr)

    return {"status": "succesfully stored pull request"}
