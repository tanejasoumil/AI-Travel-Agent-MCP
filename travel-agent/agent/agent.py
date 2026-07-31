import asyncio
import uuid

from agent.graph import build_agent


def message_text(message) -> str:
    """Convert a LangChain message's content into readable terminal text."""

    content = getattr(message, "content", "")

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                text = item.get("text")
                if text:
                    parts.append(str(text))
        return "\n".join(parts)

    return str(content)


async def main() -> None:
    agent, tools = await build_agent()

    print("\nLoaded MCP tools:")
    for tool in tools:
        print(f"  - {tool.name}")

    thread_id = str(uuid.uuid4())

    print("\nTravel Agent is ready.")
    print("Commands: /new starts a new conversation, /tools lists tools, exit quits.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nTravel Agent stopped.")
            return

        if not question:
            continue

        if question.lower() in {"exit", "quit", "/exit"}:
            print("Travel Agent stopped.")
            return

        if question.lower() == "/new":
            thread_id = str(uuid.uuid4())
            print("Started a new conversation.\n")
            continue

        if question.lower() == "/tools":
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")
            print()
            continue

        try:
            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": question}]},
                config={"configurable": {"thread_id": thread_id}},
            )

            final_message = result["messages"][-1]
            print(f"\nAssistant: {message_text(final_message)}\n")

        except Exception as exc:
            print(f"\nAgent error: {exc}\n")
            print(
                "Check that Ollama is running and that the configured model "
                "has been downloaded.\n"
            )


if __name__ == "__main__":
    asyncio.run(main())
