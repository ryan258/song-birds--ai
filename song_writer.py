# File: song_writer.py

import logging
from logger import setup_logger

setup_logger()

class SongWriter:
    def __init__(self, lyricist, composer):
        self.lyricist = lyricist
        self.composer = composer

    async def create_initial_draft(self, theme):
        lyrics = await self.lyricist.generate_lyrics(theme)
        
        if lyrics is None:
            logging.error("Failed to generate lyrics. Please try again.")
            return {"error": "Failed to generate lyrics. Please try again."}

        if len(lyrics) < 50:  # Check for sufficient lyrics
            logging.error("Generated lyrics were too short. Please try again.")
            return {"error": "Generated lyrics were too short. Please try again."}

        style_description = await self.composer.create_style_description(lyrics)
        
        if style_description is None:
            logging.error("Failed to generate style description. Please try again.")
            return {"error": "Failed to generate style description. Please try again."}

        song = {
            "lyrics": lyrics,
            "style_description": style_description
        }
        logging.info(f"Created initial draft:\n\nLyrics:\n{lyrics}\n\nStyle Description:\n{style_description}")
        
        return song

    async def refine_song(self, current_song, lyrics_feedback, style_feedback):
        refined_lyrics = await self.lyricist.refine_lyrics(
            current_song['lyrics'], 
            lyrics_feedback
        )
        
        if refined_lyrics is None:
            logging.error("Failed to refine lyrics. Please try again with different feedback.")
            return {"error": "Failed to refine lyrics. Please try again with different feedback."}

        if len(refined_lyrics) < 50:
            logging.error("Refined lyrics were too short. Please try again with different feedback.")
            return {"error": "Refined lyrics were too short. Please try again with different feedback."}

        refined_style = await self.composer.refine_style_description(
            current_song['style_description'], 
            style_feedback
        )
        
        if refined_style is None:
            logging.error("Failed to refine style description. Please try again with different feedback.")
            return {"error": "Failed to refine style description. Please try again with different feedback."}

        refined_song = {
            "lyrics": refined_lyrics,
            "style_description": refined_style
        }
        logging.info(f"Refined song:\n\nLyrics:\n{refined_lyrics}\n\nStyle Description:\n{refined_style}")
        
        return refined_song