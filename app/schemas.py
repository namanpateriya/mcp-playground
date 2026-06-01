from pydantic import BaseModel
from typing import Optional


class ProjectStatus(BaseModel):

    project_name: str
    health: str
    timeline: str
    summary: str


class ProjectRisk(BaseModel):

    risk_id: str
    description: str
    severity: str


class StatusReportRequest(BaseModel):

    include_risks: bool = True
    include_timeline: bool = True


class ToolResponse(BaseModel):

    success: bool
    message: str
    data: Optional[dict] = None
