import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

load_dotenv()

CONFIG = {
    "mcpServers": {
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "C:\\Users\\David\\Desktop\\MCP"
           ]
        },
        "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"],
            "env": {"DISPLAY": ":1"}  
        }
    }
}

async def main():
    client = MCPClient.from_dict(CONFIG)
    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = MCPAgent(llm=llm, client=client, max_steps=20)

    result = await agent.run("Busca en Google la mejor cafetería de especialidad en Santiago de Compostela. Guarda el resultado en un fichero md bien formateado.")
    print("\n🔥 Result:", result)
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())