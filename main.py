# 🎵 File: main.py 🎵

import asyncio
from song_writer import SongWriter
from lyricist import Lyricist
from composer import Composer
from ollama import Ollama
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='frontend')

class AIAssistant:
    def __init__(self):
        self.ollama = Ollama(model="llama3.1:latest")
        self.lyricist = Lyricist(self.ollama)
        self.composer = Composer(self.ollama)
        self.song_writer = SongWriter(self.lyricist, self.composer)
        self.current_song = None

    async def write_initial_draft(self, theme):
        print(f"🌟 Starting to write an initial draft about {theme}!")
        self.current_song = await self.song_writer.create_initial_draft(theme)
        print("📝 Initial draft is ready!")
        return self.current_song

    async def refine_song(self, theme, lyrics_refine, melody_adjust):
        if not self.current_song:
            raise ValueError("No initial draft to refine. Please create an initial draft first.")
        
        print(f"🔄 Refining the song about {theme}!")
        self.current_song = await self.song_writer.refine_song(self.current_song, lyrics_refine, melody_adjust)
        print("🎉 Refined song is ready!")
        return self.current_song

assistant = AIAssistant()

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/write_initial_draft', methods=['POST'])
def write_initial_draft():
    data = request.json
    theme = data['theme']
    
    song = asyncio.run(assistant.write_initial_draft(theme))
    
    return jsonify(song)

@app.route('/refine_song', methods=['POST'])
def refine_song():
    data = request.json
    theme = data['theme']
    lyrics_refine = data.get('lyricsRefine', "Make it more upbeat")
    melody_adjust = data.get('melodyAdjust', "Add more rhythm")
    
    try:
        song = asyncio.run(assistant.refine_song(theme, lyrics_refine, melody_adjust))
        return jsonify(song)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)