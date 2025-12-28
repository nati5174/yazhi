from fastapi import APIRouter, Request,Depends
from db.services import store_pull_request
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import SessionLocal
from services.github import get_installation_token, get_pull_request_files

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
        repo_name = payload["repository"]["name"]
        sha = payload["pull_request"]["head"]["sha"]
        action = payload["action"]

        ctx = {
                "pr_number": pr_number,
                "repo_name": repo_name,
                "sha": sha,
                "action": action
        }

        result =  await store_pull_request(ctx, db)

        installation_id = payload["installation"]["id"]
        owner = payload["pull_request"]["user"]["login"]
        installation_token = await get_installation_token(installation_id)
        pull_request_diff = await get_pull_request_files(owner, repo_name, pr_number, installation_token)

        print(pull_request_diff)
        return pull_request_diff