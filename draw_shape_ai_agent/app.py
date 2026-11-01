from agents.drawing_agent import drawShapesPrompt
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(drawShapesPrompt(prompt=prompt))
