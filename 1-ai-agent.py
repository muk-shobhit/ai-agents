from phi.agent import Agent
from phi.model.azure import AzureOpenAIChat
from dotenv import load_dotenv
import os

load_dotenv()

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

agent=Agent(
   model=AzureOpenAIChat(id="gpt-4",  azure_endpoint=azure_endpoint, azure_deployment="gpt-4")
)

agent.print_response("What is AI Agent?", stream=True)