# 📝 File: lyricist.py 📝
import logging
from logger import setup_logger

setup_logger()

class Lyricist:
    def __init__(self, ollama):
        # 🤖 Our AI model
        self.ollama = ollama

    async def generate_lyrics(self, theme):
        # 💡 Ask our AI to write lyrics
        prompt = f"""Write lyrics for a song about {theme}. Follow these guidelines:
1. Choose an appropriate genre based on the theme.
2. Create a song structure typical for that genre (e.g., Verse-Chorus-Verse-Chorus-Bridge-Chorus for pop).
3. Clearly label each section with [Verse], [Chorus], [Bridge], etc.
4. Include vivid imagery and emotional language.
5. Ensure a coherent narrative or message throughout the song.
6. Use rhyme schemes appropriate for the chosen genre.
7. Aim for 2-3 verses, 1 chorus (repeated 2-3 times), and optionally a bridge.
8. Keep the total length between 20-30 lines.

Begin your response with the chosen genre, then provide the lyrics.
"""
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        # ✨ Clean up the lyrics
        lyrics = response.strip()
        
        print("✏️ Lyrics are ready!")
        logging.info(f"Generated lyrics for theme '{theme}': {lyrics}")

        return lyrics

    async def refine_lyrics(self, lyrics, feedback):
        # 🔧 Improve the lyrics based on feedback
        prompt = f"""Refine these lyrics based on the following feedback:

Original Lyrics:
{lyrics}

Feedback: {feedback}

Please apply the feedback while maintaining the original structure and essence of the song. Ensure you:
1. Preserve the genre and overall theme.
2. Maintain consistent labeling of sections ([Verse], [Chorus], etc.).
3. Improve imagery, emotional impact, and wordplay where possible.
4. Enhance the rhyme scheme and flow if needed.
5. Address any specific points mentioned in the feedback.
6. If adding or removing lines, ensure the song structure remains balanced.

Provide the refined lyrics with clear section labels.
"""
        
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        refined_lyrics = response.strip()
        
        print("🎨 Lyrics have been polished!")
        logging.info(f"Refined lyrics based on feedback '{feedback}': {refined_lyrics}")
        return refined_lyrics