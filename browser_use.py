import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient


async def main():
    load_dotenv()

    client = MCPClient.from_config_file("browser_mcp.json")

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    result = await agent.run(
        "Open https://httpbin.org/ip and tell me my IP address.",
        max_steps=30,
    )
    print(f"\nResult: {result}")


if __name__ == "__main__":
    asyncio.run(main())
