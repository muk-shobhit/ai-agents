from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.model.azure import AzureOpenAIChat
import os
load_dotenv()


def get_company_symbol(company: str) -> str:
        """
        Use this function to get the symbol for a company.

        Args:
            company (str): The name of the company.

        Returns:
            str: The symbol for the company.
        """
        symbols= {
            "Facebook": "FB",
            "Apple": "AAPL",
            "Amazon": "AMZN",
            "Netflix": "NFLX",
            "Google": "GOOGL",
            "Microsoft": "MSFT",
            "A0012": "TSLA"
        }
        return symbols.get(company, "Invalid Company")

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

agent=Agent(
    model=AzureOpenAIChat(id="gpt-4",  azure_endpoint=azure_endpoint, azure_deployment="gpt-4"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    instructions=["Use tables to display the data", "If you dont know the company symbol, use the get_company_symbol function to get it"]
)

agent.print_response("Whats the current stock price for A0012 today?", stream=True)