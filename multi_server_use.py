import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient


async def main():
    load_dotenv()

    client = MCPClient.from_config_file("multi_server_config.json")

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    result = await agent.run(
        "Open https://httpbin.org/ip, get the IP and save it to a file named ip.txt.",
        max_steps=30,
    )
    print(f"\nResult: {result}")


if __name__ == "__main__":
    asyncio.run(main())
