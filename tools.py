import os
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> None:
        return None

load_dotenv()

try:
    from langchain_core.tools import tool
except ImportError:
    def tool(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

try:
    from tavily import TavilyClient
except ImportError:
    TavilyClient = None


def _get_tavily_client():
    api_key = os.getenv("TAVILY_API_KEY") or os.getenv("TAVILIY_API_KEY")
    if not api_key:
        raise RuntimeError("TAVILY_API_KEY is not set. Add it to your environment or .env file.")
    if TavilyClient is None:
        raise RuntimeError("The 'tavily' package is not installed. Install dependencies first.")
    return TavilyClient(api_key=api_key)


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Return titles, URLs, and snippets."""
    try:
        tavily = _get_tavily_client()
        results = tavily.search(query=query, max_results=5)
        return str(results)
    except Exception as exc:
        return f"Search failed: {exc}"


if __name__ == "__main__":
    result = web_search.invoke("what are the recent news of war?") if hasattr(web_search, "invoke") else web_search("what are the recent news of war?")
    print(result)
        