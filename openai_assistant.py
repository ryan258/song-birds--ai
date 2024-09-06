# File: openai_assistant.py

import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

# Load the special secrets from our .env file
load_dotenv()

# This is like a secret code that lets us talk to OpenAI's super smart computer
API_KEY = os.getenv("OPENAI_API_KEY")

# If we don't have the secret code, we tell the user how to get it
if not API_KEY:
    print("Oops! We need a special key to talk to the AI.")
    print("Ask a grown-up to help you get an 'OPENAI_API_KEY'.")
    print("Then, create a file named '.env' in the same folder as this script.")
    print("In that file, write: OPENAI_API_KEY=your_key_here")
    print("Replace 'your_key_here' with the actual key you got.")
    exit(1)

# We create a special helper that knows how to talk to OpenAI
client = AsyncOpenAI(api_key=API_KEY)

class OpenAIAssistant:
    def __init__(self):
        # This is like telling the AI what kind of helper we want
        self.model = "gpt-3.5-turbo"
    
    async def generate(self, prompt):
        try:
            # We're asking the AI to help us with our prompt
            response = await client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": """You are an AI assistant specialized in songwriting and music production. Your primary functions include:

1. Generating creative and emotionally resonant song lyrics based on given themes.
2. Crafting innovative musical style descriptions that complement lyrics.
3. Refining and improving existing lyrics and musical styles based on feedback.
4. Providing insightful suggestions and explanations related to songwriting and music production.

Approach each task with creativity, technical expertise, and a deep understanding of various musical genres and songwriting techniques. Your responses should be detailed, engaging, and tailored to inspire both novice and experienced songwriters and producers."""},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # The AI gives us back an answer, and we're picking out just the text part
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            # If something goes wrong, we tell the user what happened
            print(f"Oops! Something went wrong when talking to the AI: {str(e)}")
            return None

# This is a test to make sure our code works
if __name__ == "__main__":
    assistant = OpenAIAssistant()
    
    # We're going to ask the AI a fun question
    prompt = "Tell me a short, funny joke about programming for kids."
    
    # We use this special code to run our 'generate' function
    result = asyncio.run(assistant.generate(prompt))
    
    if result:
        print("The AI said:")
        print(result)
    else:
        print("Sorry, the AI couldn't come up with a joke this time.")