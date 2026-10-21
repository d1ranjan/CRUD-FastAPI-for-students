"""FastAPI application entry point."""
from fastapi import FastAPI

from app.database import Base, engine
from app import model  # noqa: F401 - register SQLAlchemy models
from app.routes.base import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="CRUD API for student records using FastAPI and SQLite.",
    version="1.0.0",
)
app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Student Management API. Visit /docs for Swagger UI."}


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
