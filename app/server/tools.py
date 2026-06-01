from app.server.resources import (
    PROJECT_STATUS,
    PROJECT_RISKS,
    PROJECT_TIMELINE
)


def summarize_project():

    return {
        "project_name": PROJECT_STATUS["project_name"],
        "summary": PROJECT_STATUS["summary"],
        "health": PROJECT_STATUS["health"]
    }


def calculate_project_health(
    risk_count: int = 0
):

    if risk_count >= 3:
        return {"health": "Red"}

    if risk_count >= 1:
        return {"health": "Amber"}

    return {"health": "Green"}


def generate_status_report(
    include_risks: bool = True,
    include_timeline: bool = True
):

    report = {
        "status": PROJECT_STATUS
    }

    if include_risks:
        report["risks"] = PROJECT_RISKS

    if include_timeline:
        report["timeline"] = PROJECT_TIMELINE

    return report
