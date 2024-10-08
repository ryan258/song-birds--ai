# File: main.py

from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env

from flask import Flask, request, jsonify, send_from_directory
import asyncio
from song_writer import SongWriter
from lyricist import Lyricist
from composer import Composer
from ollama import Ollama
from openai_assistant import OpenAIAssistant

# Create our web app
app = Flask(__name__, static_folder='frontend')

# This is like a helper that knows how to write songs
class AIAssistant:
    def __init__(self, ai_type="openai"):
        # Set up our AI tools
        if ai_type == "ollama":
            self.ai = Ollama(model="llama3.1:latest")
        elif ai_type == "openai":
            self.ai = OpenAIAssistant()
        else:
            raise ValueError("Unknown AI type. Please choose 'ollama' or 'openai'.")
        
        self.lyricist = Lyricist(self.ai)
        self.composer = Composer(self.ai)
        self.song_writer = SongWriter(self.lyricist, self.composer)
        self.current_song = None

    # This writes a new song
    async def write_initial_draft(self, theme):
        print(f"Starting to write a song about {theme}!")
        self.current_song = await self.song_writer.create_initial_draft(theme)
        print("Song is ready!")
        return self.current_song

    # This makes the song better based on feedback
    async def refine_song(self, lyrics_feedback, style_feedback):
        if not self.current_song:
            raise ValueError("No song to make better. Please write a song first.")
        
        print("Making the song better!")
        self.current_song = await self.song_writer.refine_song(
            self.current_song,
            lyrics_feedback,
            style_feedback
        )
        print("Improved song is ready!")
        return self.current_song

# Create our AI helper (you can change "ollama" to "openai" to use OpenAI instead)
assistant = AIAssistant("openai")

# When someone visits our website, show them the main page
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# When someone wants a new song, make one
@app.route('/write_initial_draft', methods=['POST'])
def write_initial_draft():
    data = request.json
    theme = data['theme']
    
    song = asyncio.run(assistant.write_initial_draft(theme))
    
    return jsonify(song)

# When someone wants to make their song better, do that
@app.route('/refine_song', methods=['POST'])
def refine_song():
    data = request.json
    lyrics_feedback = data.get('lyricsFeedback', "")
    style_feedback = data.get('styleFeedback', "")
    
    try:
        song = asyncio.run(assistant.refine_song(lyrics_feedback, style_feedback))
        return jsonify(song)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Start our app when we run this file
if __name__ == "__main__":
    app.run(debug=True)