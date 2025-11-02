import wikipedia
from duckduckgo_search import DDGS
from typing import Optional


class WikipediaSearchTool:
    """Tool for searching Wikipedia."""

    def search(self, query: str) -> str:
        """Search Wikipedia and return a summary."""
        try:
            # Search Wikipedia
            results = wikipedia.search(query, results=3)

            if not results:
                return f"No Wikipedia results found for '{query}'"

            # Get summary of the first result
            try:
                summary = wikipedia.summary(results[0], sentences=5)
                return f"Wikipedia Summary for '{results[0]}':\n{summary}"
            except wikipedia.exceptions.DisambiguationError as e:
                # If disambiguation, try the first option
                try:
                    summary = wikipedia.summary(e.options[0], sentences=5)
                    return f"Wikipedia Summary for '{e.options[0]}':\n{summary}"
                except:
                    return f"Found multiple results: {', '.join(results[:3])}"
            except wikipedia.exceptions.PageError:
                return f"No Wikipedia page found for '{query}'"

        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"


class DuckDuckGoSearchTool:
    """Tool for searching the web using DuckDuckGo."""

    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 5) -> str:
        """Search DuckDuckGo and return results."""
        try:
            results = self.ddgs.text(query, max_results=max_results)

            if not results:
                return f"No search results found for '{query}'"

            # Format results
            formatted_results = f"DuckDuckGo Search Results for '{query}':\n\n"

            for i, result in enumerate(results, 1):
                title = result.get("title", "No title")
                body = result.get("body", "No description")
                formatted_results += f"{i}. {title}\n{body}\n\n"

            return formatted_results.strip()

        except Exception as e:
            return f"Error searching DuckDuckGo: {str(e)}"
