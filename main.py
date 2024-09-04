# 🎵 File: main.py 🎵

import asyncio
from song_writer import SongWriter
from lyricist import Lyricist
from composer import Composer
from ollama import Ollama  # Import the Ollama class

# 🤖 Our AI assistant class
class AIAssistant:
    def __init__(self):
        # 🔧 Set up our Ollama model
        self.ollama = Ollama(model="llama3.1:latest")  # Create an instance of Ollama
        
        # 👥 Create our team of agents
        self.lyricist = Lyricist(self.ollama)
        self.composer = Composer(self.ollama)
        self.song_writer = SongWriter(self.lyricist, self.composer)

    async def write_song(self, theme):
        # 🎶 Let's make some music!
        print(f"🌟 Starting to write a song about {theme}!")
        song = await self.song_writer.create_song(theme)
        print("🎉 Song is ready!")
        return song

# 🚀 Main function to run our program
async def main():
    assistant = AIAssistant()
    song = await assistant.write_song("friendship")
    print("📜 Here's our song:")
    print(song)

# 🏁 Run the main function
if __name__ == "__main__":
    asyncio.run(main())