from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

from agent.config import Settings
from agent.mcp_client import create_mcp_client
from agent.prompts import SYSTEM_PROMPT


async def build_agent():
    """Build the LangGraph-backed agent and load MCP tools."""

    settings = Settings()
    client = create_mcp_client()
    tools = await client.get_tools()

    model = ChatOllama(
        model=settings.ollama_model,
        base_url=settings.ollama_base_url,
        temperature=settings.temperature,
    )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),
    )

    return agent, tools
