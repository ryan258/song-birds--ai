import logging
from logger import setup_logger

setup_logger()

class SongWriter:
    def __init__(self, lyricist, composer):
        self.lyricist = lyricist
        self.composer = composer

    async def create_initial_draft(self, theme):
        lyrics = await self.lyricist.generate_lyrics(theme)
        
        if not lyrics or len(lyrics) < 50:  # Check for sufficient lyrics
            logging.error(f"Insufficient lyrics generated for theme: {theme}")
            return {"error": "Failed to generate sufficient lyrics. Please try again."}

        style_description = await self.composer.create_style_description(lyrics)
        
        if style_description.startswith("Error:"):
            logging.error(f"Failed to generate style description: {style_description}")
            return {"error": style_description}

        song = {
            "lyrics": lyrics,
            "style_description": style_description
        }
        logging.info(f"Created initial draft with theme '{theme}': {song}")
        
        return song

    async def refine_song(self, current_song, lyrics_feedback, style_feedback):
        refined_lyrics = await self.lyricist.refine_lyrics(
            current_song['lyrics'], 
            lyrics_feedback
        )
        
        if not refined_lyrics or len(refined_lyrics) < 50:
            logging.error("Refinement resulted in insufficient lyrics")
            return {"error": "Refinement failed. Please try different feedback."}

        refined_style = await self.composer.refine_style_description(
            current_song['style_description'], 
            style_feedback
        )
        
        if refined_style.startswith("Error:"):
            logging.error(f"Failed to refine style description: {refined_style}")
            return {"error": refined_style}

        refined_song = {
            "lyrics": refined_lyrics,
            "style_description": refined_style
        }
        logging.info(f"Refined song: {refined_song}")
        
        return refined_song