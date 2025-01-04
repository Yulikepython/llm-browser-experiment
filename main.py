from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

TASK_PROMPT = ""
MODEL = "gpt-4o"

async def main():
    agent = Agent(
        task=TASK_PROMPT,
        llm=ChatOpenAI(model=MODEL),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())