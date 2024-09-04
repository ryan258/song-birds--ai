# 🎵 File: main.py 🎵

import asyncio
from song_writer import SongWriter
from lyricist import Lyricist
from composer import Composer
from ollama import Ollama
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__, static_folder='frontend')

# 🤖 Our AI assistant class
class AIAssistant:
    def __init__(self):
        # 🔧 Set up our Ollama model
        self.ollama = Ollama(model="llama3.1:latest")
        
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

assistant = AIAssistant()

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/write_song', methods=['POST'])
def write_song():
    theme = request.json['theme']
    song = asyncio.run(assistant.write_song(theme))
    # Ensure song is a dictionary with 'lyrics' and 'melody' keys
    if isinstance(song, str):
        # If song is a single string, split it into lyrics and melody
        parts = song.split("\n\nMelody:\n\n")
        lyrics = parts[0].replace("Lyrics:\n\n", "")
        melody = parts[1] if len(parts) > 1 else "Melody not provided"
        song = {"lyrics": lyrics, "melody": melody}
    return jsonify(song)

if __name__ == "__main__":
    app.run(debug=True)