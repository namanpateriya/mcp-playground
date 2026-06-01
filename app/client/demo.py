import asyncio

from app.client.mcp_client import (
    MCPProjectClient
)


async def main():

    client = MCPProjectClient()

    await client.connect()

    print("\n=== RESOURCES ===\n")

    resources = await client.list_resources()

    print(resources)

    print("\n=== STATUS RESOURCE ===\n")

    status = await client.read_resource(
        "project://status"
    )

    print(status)

    print("\n=== TOOLS ===\n")

    tools = await client.list_tools()

    print(tools)

    print("\n=== HEALTH TOOL ===\n")

    health = await client.call_tool(
        "calculate_project_health",
        {
            "risk_count": 3
        }
    )

    print(health)

    print("\n=== STATUS REPORT ===\n")

    report = await client.call_tool(
        "generate_status_report",
        {
            "include_risks": True,
            "include_timeline": True
        }
    )

    print(report)

    await client.close()


if __name__ == "__main__":

    asyncio.run(main())
