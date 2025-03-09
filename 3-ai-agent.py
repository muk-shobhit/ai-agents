from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.model.azure import AzureOpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import os

load_dotenv()

web_agent=Agent(
    name="Web Agent",
    model=AzureOpenAIChat(id="gpt-4",  azure_endpoint="https://myopenai121.openai.azure.com/", azure_deployment="gpt-4"),
    tools=[DuckDuckGo()],
    markdown=True,
    instructions=["Always include sources"]
)


finance_agent=Agent(
    model=AzureOpenAIChat(id="gpt-4",  azure_endpoint="https://myopenai121.openai.azure.com/", azure_deployment="gpt-4"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    instructions=["Use tables to display the data"]
)

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

agent_team=Agent(
    name="Team Agent",
    model=AzureOpenAIChat(id="gpt-4",  azure_endpoint=azure_endpoint, azure_deployment="gpt-4"),
    markdown=True,
    agents=[web_agent, finance_agent],
    instructions=["Always include sources","Use tables to display the data"]
)

agent_team.print_response("Summarize the analyst recommendation for Apple", stream=True)