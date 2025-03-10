from phi.agent import Agent
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.model.azure import AzureOpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import os

load_dotenv()

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_deployment=os.getenv("AZURE_OPENAI_API_DEPLOYMENT")

web_agent=Agent(
    name="Web Agent",
    model=AzureOpenAIChat(id="webagent",  azure_endpoint=azure_endpoint, azure_deployment=azure_deployment),
    tools=[DuckDuckGo()],
    markdown=True,
    instructions=["Always include sources"],
    show_tool_calls=True
)


finance_agent=Agent(
    model=AzureOpenAIChat(id="finance-agent",  azure_endpoint=azure_endpoint, azure_deployment=azure_deployment),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    markdown=True,
    show_tool_calls=True,
    instructions=["Use tables to display the data"]
)

agent_team=Agent(
    name="Team Agent",
    model=AzureOpenAIChat(id="team-agent",  azure_endpoint=azure_endpoint, azure_deployment=azure_deployment),
    markdown=True,
    agents=[web_agent, finance_agent],
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    debug_mode=True
)

while True:
    user_input = input("Enter your prompt (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    agent_team.print_response(user_input, stream=True)