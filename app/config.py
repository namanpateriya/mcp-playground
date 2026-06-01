from dotenv import load_dotenv
import os

load_dotenv()

SERVER_NAME = os.getenv(
    "SERVER_NAME",
    "Project Management MCP Server"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)
