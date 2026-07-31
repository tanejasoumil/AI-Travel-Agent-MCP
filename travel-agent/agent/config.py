from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the local travel agent."""

    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    temperature: float = float(os.getenv("OLLAMA_TEMPERATURE", "0"))
