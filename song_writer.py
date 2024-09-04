# 🎸 File: song_writer.py 🎸
import logging
from logger import setup_logger

setup_logger()

class SongWriter:
    def __init__(self, lyricist, composer):
        # 👥 Our team of specialists
        self.lyricist = lyricist
        self.composer = composer

    async def create_song(self, theme):
        # 📝 Step 1: Write the lyrics
        lyrics = await self.lyricist.generate_lyrics(theme)
        
        # 🎵 Step 2: Compose the melody
        melody = await self.composer.create_melody(lyrics)
        
        # 🔄 Step 3: Refine and adjust
        lyrics = await self.lyricist.refine_lyrics(lyrics, "Make it more upbeat")
        melody = await self.composer.adjust_melody(melody, "Add more rhythm")
        
        # 🎶 Step 4: Put it all together
        song = {
            "lyrics": lyrics,
            "melody": melody
        }
        logging.info(f"Created song with theme '{theme}': {song}")
        
        return song