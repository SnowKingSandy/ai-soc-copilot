from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.schemas.log_schema import LogRequest
from app.schemas.incident_schema import IncidentResponse

from app.services.workflow_service import analyze_log
from app.services.incident_service import (
    save_incident,
    get_all_incidents,
    delete_incident,
)
from app.services.stats_service import get_stats

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI SOC Copilot",
    description="AI-powered Security Operations Center Copilot",
    version="1.0.0",
)

# CORS configuration for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "SOC Copilot Running",
        "status": "healthy",
    }


@app.post(
    "/analyze",
    response_model=IncidentResponse,
)
def analyze(request: LogRequest):
    result = analyze_log(request.log_text)

    save_incident(result)

    return result


@app.get("/incidents")
def get_incidents():
    incidents = get_all_incidents()

    return incidents


@app.delete("/incidents/{incident_id}")
def remove_incident(incident_id: int):
    delete_incident(incident_id)

    return {
        "message": "deleted",
    }


@app.get("/stats")
def stats():
    return get_stats()