from tools.drawing_tools import getTools
from prompts.drawing_system_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv 
from pydantic_ai import Agent 

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    system_prompt = SYSTEM_PROMPT,
    tools = getTools()
)

async def drawShapesPrompt(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')