# 🤖 File: ollama.py 🤖

import aiohttp
import json

class Ollama:
    def __init__(self, model="llama3.1:latest"):
        # 🏠 The base URL for the Ollama API
        self.base_url = "http://localhost:11434/api/generate"
        # 🎭 The model we're using
        self.model = model

    async def generate(self, prompt):
        # 📦 Package up our request
        data = {
            "model": self.model,
            "prompt": prompt
        }

        # 🌐 Send our request to Ollama
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, json=data) as response:
                # 🎉 Check if we got a good response
                if response.status == 200:
                    # 📚 Read the response content
                    content = await response.text()
                    # 🧩 Put the pieces together
                    result = self.process_response(content)
                    return result
                else:
                    # 😢 Uh oh, something went wrong
                    raise Exception(f"Error: Received status code {response.status}")

    def process_response(self, content):
        # 🎨 Clean up and combine the response
        lines = content.strip().split('\n')
        full_response = ""
        for line in lines:
            try:
                response_part = json.loads(line)
                full_response += response_part['response']
            except json.JSONDecodeError:
                print(f"Warning: Couldn't parse line: {line}")
        return full_response.strip()