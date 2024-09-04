# 🎸 File: song_writer.py 🎸
import logging
from logger import setup_logger

setup_logger()

class SongWriter:
    def __init__(self, lyricist, composer):
        self.lyricist = lyricist
        self.composer = composer

    async def create_initial_draft(self, theme):
        # 📝 Step 1: Write initial lyrics
        lyrics = await self.lyricist.generate_lyrics(theme)
        
        # 🎵 Step 2: Compose initial melody
        melody = await self.composer.create_melody(lyrics)
        
        # 🎶 Step 3: Put it all together
        song = {
            "lyrics": lyrics,
            "melody": melody
        }
        logging.info(f"Created initial draft with theme '{theme}': {song}")
        
        return song

    async def refine_song(self, current_song, lyrics_refine, melody_adjust):
        # 🔄 Step 1: Refine and adjust based on current version
        refined_lyrics = await self.lyricist.refine_lyrics(current_song['lyrics'], lyrics_refine)
        refined_melody = await self.composer.adjust_melody(current_song['melody'], melody_adjust)
        
        # 🎶 Step 2: Put it all together
        refined_song = {
            "lyrics": refined_lyrics,
            "melody": refined_melody
        }
        logging.info(f"Refined song: {refined_song}")
        
        return refined_song