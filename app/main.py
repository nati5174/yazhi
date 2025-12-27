from fastapi import FastAPI
from api.webhook import router as webhook_router


app = FastAPI()

app.include_router(webhook_router, prefix="/github-webhook")

@app.get("/health")
async def root():
    return {"status": "ok"}