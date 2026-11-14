import webbrowser
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agents.orchestrator import get_compliance_agent

agent_executor = None


class AuditRequest(BaseModel):
    query: str


class AuditResponse(BaseModel):
    status: str
    audit_report: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    global agent_executor
    agent_executor = get_compliance_agent()
    webbrowser.open("http://127.0.0.1:8000/docs")
    yield


app = FastAPI(
    title="Autonomous Compliance & Data Auditor API",
    version="1.0.0",
    description="Agentic AI API for regulatory audit workflows.",
    lifespan=lifespan,
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "compliance-agent-auditor"}


@app.post("/api/audit", response_model=AuditResponse)
async def run_audit(request: AuditRequest):
    if not agent_executor:
        raise HTTPException(
            status_code=500,
            detail="Agent initialize nahi hua. GROQ_API_KEY check karein.",
        )
    try:
        result = await agent_executor.ainvoke(
            {"messages": [("user", request.query)]}
        )
        report = result["messages"][-1].content
        return AuditResponse(status="success", audit_report=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))