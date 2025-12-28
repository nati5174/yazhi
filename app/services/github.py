import time
import httpx
import asyncio
import os
import jwt
from dotenv import load_dotenv

load_dotenv()

GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")
with open(os.getenv("GITHUB_PRIVATE_KEY_PATH"), "r") as f:
    GITHUB_PRIVATE_KEY = f.read()

async def generate_jwt_token() -> str:

    iat = int(time.time()) - 60
    exp = int(time.time()) + (60*10)
    payload = {
        "iat": iat,
        "exp": exp,
        "iss": GITHUB_APP_ID
    }

    token = jwt.encode(payload, GITHUB_PRIVATE_KEY, algorithm="RS256")
    
    return token

async def get_installation_token(installation_id: int):

    jwt_token = await generate_jwt_token()
    headers = {"Authorization": f"Bearer {jwt_token}",
            "Accept": "application/vnd.github+json"

    }    
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        token = data["token"]
        return token

async def get_pull_request_files(owner, repo, pull_number, installation_token):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    headers = {
        "Authorization": f"Bearer {installation_token}",
        "Accept": "application/vnd.github+json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data


 

