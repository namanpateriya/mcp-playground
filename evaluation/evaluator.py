import asyncio

from app.client.mcp_client import MCPProjectClient


async def evaluate():

    results = []

    client = MCPProjectClient()

    await client.connect()

    try:

        resources = await client.list_resources()

        results.append({
            "test": "resource_discovery",
            "passed": resources is not None
        })

        tools = await client.list_tools()

        results.append({
            "test": "tool_discovery",
            "passed": tools is not None
        })

        status = await client.read_resource(
            "project://status"
        )

        results.append({
            "test": "resource_read",
            "passed": status is not None
        })

        report = await client.call_tool(
            "generate_status_report",
            {
                "include_risks": True,
                "include_timeline": True
            }
        )

        results.append({
            "test": "tool_execution",
            "passed": report is not None
        })

        health = await client.call_tool(
            "calculate_project_health",
            {
                "risk_count": 3
            }
        )

        results.append({
            "test": "tool_arguments",
            "passed": health is not None
        })

    finally:

        await client.close()

    return results


if __name__ == "__main__":

    output = asyncio.run(
        evaluate()
    )

    print("\n=== MCP EVALUATION ===\n")

    for result in output:
        print(result)
