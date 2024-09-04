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

    async def refine_song(self, theme, lyrics_refine, melody_adjust):
        # 📝 Step 1: Get the initial draft
        initial_draft = await self.create_initial_draft(theme)
        
        # 🔄 Step 2: Refine and adjust
        refined_lyrics = await self.lyricist.refine_lyrics(initial_draft['lyrics'], lyrics_refine)
        refined_melody = await self.composer.adjust_melody(initial_draft['melody'], melody_adjust)
        
        # 🎶 Step 3: Put it all together
        refined_song = {
            "lyrics": refined_lyrics,
            "melody": refined_melody
        }
        logging.info(f"Refined song with theme '{theme}': {refined_song}")
        
        return refined_song