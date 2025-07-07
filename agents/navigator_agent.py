from langchain_community.chat_models import ChatOllama


class NavigatorAgent:
    def __init__(self):
        self.llm = ChatOllama(model="llama3")

    def interpret_html(self, html_content, goal="scrape users"):
        prompt = f"""
        You are an AI agent navigating a SaaS admin portal.
        Your goal is: {goal}.
        Below is the HTML of the page.
        Identify any tables or forms relevant to the goal and suggest selectors.

        HTML:
        {html_content[:5000]}  # Trimmed for context
        """
        response = self.llm.invoke(prompt)
        return response.content
