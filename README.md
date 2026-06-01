# MCP Playground

MCP Playground is a learning-focused repository designed to explore the Model Context Protocol (MCP) through a practical project management use case.

The repository demonstrates how MCP clients and servers communicate using standardized resources and tools, enabling discoverable and interoperable AI systems.

Rather than building another AI application, this repository focuses on understanding an emerging protocol that is increasingly being adopted for connecting AI models with external systems and capabilities.

---

# Why MCP?

As AI systems become more capable, they need access to external information and actions.

Traditional approaches typically rely on:

* custom API integrations
* hardcoded tool definitions
* framework-specific implementations

These approaches work, but they create fragmented ecosystems where every integration must be built independently.

MCP introduces a standardized protocol for exposing information and functionality to AI systems.

Think of MCP as:

```text
USB-C for AI Applications
```

Instead of every model requiring a custom integration, MCP provides a common interface for discovery and execution.

---

# Features

* Real MCP Server
* Real MCP Client
* Resource Discovery
* Resource Access
* Tool Discovery
* Tool Execution
* Parameterized Tool Calls
* Evaluation Framework
* Project Management Example Use Case

---

# What This Repository Demonstrates

This repository demonstrates the foundational concepts of MCP:

### Resources

Read-only information exposed by a server.

Examples:

```text
project://status
project://risks
project://timeline
```

---

### Tools

Executable functionality exposed by a server.

Examples:

```text
summarize_project
calculate_project_health
generate_status_report
```

---

### Discovery

Clients dynamically discover:

* available resources
* available tools

without requiring prior knowledge.

---

### Client / Server Communication

The repository demonstrates how MCP clients interact with MCP servers using a standardized protocol rather than custom integrations.

---

# Architecture Overview

```text
User
 ↓
MCP Client
 ↓
MCP Server
 ├── Resources
 │    ├── project://status
 │    ├── project://risks
 │    └── project://timeline
 │
 └── Tools
      ├── summarize_project
      ├── calculate_project_health
      ├── generate_status_report
      └── server_health
```

---

# Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local environment file:

```bash
cp .env.example .env
```

---

# Running the MCP Server

```bash
python -m app.server.mcp_server
```

The server exposes:

### Resources

```text
project://status
project://risks
project://timeline
```

### Tools

```text
summarize_project
calculate_project_health
generate_status_report
server_health
```

---

# Running the Client

```bash
python -m app.client.demo
```

The demo performs:

1. Resource Discovery
2. Resource Access
3. Tool Discovery
4. Tool Execution
5. Parameterized Tool Calls

---

# Evaluation

Run:

```bash
python -m evaluation.evaluator
```

The evaluation framework validates:

* Resource Discovery
* Resource Access
* Tool Discovery
* Tool Execution
* Tool Parameter Handling

---

# Enterprise Applications

MCP can be applied across enterprise systems such as:

* Jira
* Confluence
* Salesforce
* ServiceNow
* Internal Knowledge Bases
* Workflow Platforms

Instead of building separate integrations for each AI application, organizations can expose capabilities through MCP-compatible interfaces.

---

# Learning Outcomes

After completing this repository, you should understand:

* What MCP is
* Why MCP exists
* Resources vs Tools
* MCP Clients vs Servers
* Discovery-based integrations
* Parameterized tool execution
* The role of MCP in modern AI ecosystems

---

# Future Enhancements

Potential next steps include:

* MCP + RAG
* MCP + Memory
* MCP + Multi-Agent Systems
* MCP + Enterprise Workflow Automation
* MCP + Agent Orchestration

---

# Summary

MCP Playground is a focused learning repository that demonstrates the core concepts behind the Model Context Protocol.

The goal is not to build a production system, but to develop a strong understanding of how discoverable resources and tools can be exposed through a standardized interface for AI applications.
