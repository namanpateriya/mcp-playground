# MCP Playground Walkthrough

## Start Server

```bash
python -m app.server.mcp_server
```

---

## Run Client

```bash
python -m app.client.demo
```

---

# Expected Flow

## Resource Discovery

Client discovers:

```text
project://status
project://risks
project://timeline
```

---

## Resource Reading

Client reads:

```text
project://status
```

---

## Tool Discovery

Client discovers:

```text
summarize_project
calculate_project_health
generate_status_report
server_health
```

---

## Tool Execution

Client executes:

```text
generate_status_report
```

---

## Tool Arguments

Client executes:

```text
calculate_project_health
```

with:

```json
{
  "risk_count": 3
}
```

---

# Learning Objectives

Understand:

- resources
- tools
- discovery
- execution
- MCP interoperability
