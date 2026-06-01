import json

from mcp.server.fastmcp import FastMCP

from app.config import SERVER_NAME

from app.server.resources import (
    PROJECT_STATUS,
    PROJECT_RISKS,
    PROJECT_TIMELINE
)

from app.server.tools import (
    summarize_project,
    calculate_project_health,
    generate_status_report
)

mcp = FastMCP(
    SERVER_NAME
)


# ==================================================
# RESOURCES
# ==================================================

@mcp.resource("project://status")
def project_status():

    return json.dumps(
        PROJECT_STATUS,
        indent=2
    )


@mcp.resource("project://risks")
def project_risks():

    return json.dumps(
        PROJECT_RISKS,
        indent=2
    )


@mcp.resource("project://timeline")
def project_timeline():

    return json.dumps(
        PROJECT_TIMELINE,
        indent=2
    )


# ==================================================
# TOOLS
# ==================================================

@mcp.tool(name="summarize_project")
def summarize_project_tool():

    return summarize_project()


@mcp.tool(name="calculate_project_health")
def calculate_project_health_tool(
    risk_count: int = 0
):

    return calculate_project_health(
        risk_count
    )


@mcp.tool(name="generate_status_report")
def generate_status_report_tool(
    include_risks: bool = True,
    include_timeline: bool = True
):

    return generate_status_report(
        include_risks,
        include_timeline
    )


@mcp.tool(name="server_health")
def server_health():

    return {
        "status": "healthy"
    }


if __name__ == "__main__":

    mcp.run()
