import asyncio
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()


async def main():
    # Initialize a chat agent with basic instructions
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            deployment_name=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),  # Specify the deployment name
            endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),  # Specify the endpoint
            api_key=os.getenv('AZURE_OPENAI_API_KEY'),  # Specify the API key
        ),
        name="SK-Assistant",
        instructions="You are a helpful assistant.",
    )

    # Get a response to a user message
    response = await agent.get_response(messages="Write a haiku about Semantic Kernel.")
    print(response.content)

asyncio.run(main()) 

# Output:
# Language's essence,
# Semantic threads intertwine,
# Meaning's core revealed.