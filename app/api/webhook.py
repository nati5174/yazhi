from fastapi import APIRouter, Request,Depends
from db.services import store_pull_request
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/")
async def github_webhook(req: Request, db: AsyncSession = Depends(get_db)):

        if req.headers.get('x-github-event') != "pull_request":
                return {"status": "ignored"}
                
        payload =  await req.json()

        pr_number = payload["number"]
        repo_full_name = payload["repository"]["full_name"]
        sha = payload["pull_request"]["head"]["sha"]
        action = payload["action"]

        ctx = {
                "pr_number": pr_number,
                "repo_full_name": repo_full_name,
                "sha": sha,
                "action": action
        }

        result =  await store_pull_request(ctx, db)

        print(result)
        return result