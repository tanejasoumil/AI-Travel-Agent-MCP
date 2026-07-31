# Local Travel Agent with LangGraph, Ollama, and MCP

A free local AI-agent project using Ollama, LangChain, LangGraph, FastMCP, and MCP adapters.

## Install

```bash
cd travel-agent-complete
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ollama pull llama3.2:3b
```

## Run

Make sure Ollama is running, then:

```bash
python -m agent.agent
```

The MCP client launches the FastMCP server automatically over STDIO.

## Try these prompts

```text
Recommend a beach destination in India for five days with a budget of 1000.
```

```text
My flight is 300, hotel is 500, food is 200, and activities are 150. Calculate the total.
```

```text
Build a four-day balanced itinerary for Kyoto focused on food and history.
```

Test memory with a follow-up question in the same session. Use `/new` to start a separate conversation.

## Inspect MCP

```bash
fastmcp inspect mcp_server/server.py
```

## Tests

```bash
pytest
```

## Limitations

This project does not use live flight, hotel, weather, visa, map, or exchange-rate APIs. Results are local demonstrations. The in-memory checkpointer persists only while the program is running.
