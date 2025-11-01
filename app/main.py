from fastapi import FastAPI
from app.api.router import router as research_router

app = FastAPI(title="Research Assistant API")

app.include_router(research_router)
