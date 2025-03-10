from phi.agent import Agent
from phi.model.azure import AzureOpenAIChat
from dotenv import load_dotenv
import os

load_dotenv()

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_deployment=os.getenv("AZURE_OPENAI_API_DEPLOYMENT")

agent=Agent(
   model=AzureOpenAIChat(id="gpt-4",  azure_endpoint=azure_endpoint, azure_deployment=azure_deployment)
)

agent.print_response("What is SBIN price in Stock today?", stream=True)