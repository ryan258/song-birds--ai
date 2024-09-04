# 🎼 File: composer.py 🎼
import logging
from logger import setup_logger

setup_logger()

class Composer:
    def __init__(self, ollama):
        # 🤖 Our AI model
        self.ollama = ollama

    async def create_melody(self, lyrics):
        # 🎵 Ask our AI to describe a melody
        prompt = f"""Create a melody description for these lyrics:

{lyrics}

Please follow these guidelines:
1. Analyze the mood and theme of the lyrics.
2. Choose a key signature that fits the emotional tone.
3. Determine an appropriate tempo (e.g., Andante, Allegro).
4. For each section ([Verse], [Chorus], [Bridge]):
   a. Describe the melodic contour (e.g., ascending, descending, arching).
   b. Specify pitch ranges (e.g., low, middle, high).
   c. Outline the rhythm, including note durations and any syncopation.
   d. Suggest dynamic changes (e.g., crescendo, diminuendo).
5. Indicate any repetitive melodic motifs or hooks.
6. Describe the harmony, including chord progressions if applicable.
7. Suggest instrumentation that would complement the melody.

Format your response as a structured description, clearly labeling each section of the song."""
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        melody = response.strip()
        
        print("🎶 Melody is composed!")
        logging.info(f"Created melody for lyrics: {melody}")
        return melody

    async def adjust_melody(self, melody, feedback):
        # 🔧 Improve the melody based on feedback
        prompt = f"""Adjust this melody based on the following feedback:

Original Melody Description:
{melody}

Feedback: {feedback}

Please apply the feedback while maintaining the core musical ideas. Ensure you:
1. Preserve the overall style and mood of the original melody.
2. Maintain the song structure (verse, chorus, bridge, etc.).
3. Adjust pitch, rhythm, or harmonic elements as suggested by the feedback.
4. If changing key or tempo, explain the rationale.
5. Address any specific points mentioned in the feedback.
6. Ensure the adjusted melody still complements the lyrics.

Provide the adjusted melody description with clear labels for each section.
"""
        
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        adjusted_melody = response.strip()
        
        print("🎵 Melody has been fine-tuned!")
        logging.info(f"Adjusted melody based on feedback '{feedback}': {adjusted_melody}")
        
        return adjusted_melody