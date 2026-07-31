import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient


def create_mcp_client() -> MultiServerMCPClient:
    """Create a client that launches the local FastMCP server over STDIO."""

    project_root = Path(__file__).resolve().parent.parent
    server_path = project_root / "mcp_server" / "server.py"

    return MultiServerMCPClient(
        {
            "travel_tools": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(server_path)],
            }
        }
    )
