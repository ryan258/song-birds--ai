class Composer:
    def __init__(self, ollama):
        self.ollama = ollama
        self.prompt_template = """You are a visionary music producer with an encyclopedic knowledge of genres, instruments, and production techniques. Craft a vivid, 120-character music style description for these lyrics:

{lyrics}

Consider:

1. Genre Fusion: Blend primary genre with unexpected influences.
2. Emotional Palette: Capture the lyrics' mood and any emotional shifts.
3. Rhythm & Tempo: Specify BPM range or descriptive term (e.g., "frenetic", "languid").
4. Key Instruments: Name 2-3 defining sounds, including any unique choices.
5. Production Elements: Highlight standout effects or techniques.
6. Vocal Approach: Describe the vocal style and any distinctive treatments.
7. Dynamic Journey: Hint at the song's energy progression.
8. Cultural/Era Influences: Reference specific musical periods or cultural styles.
9. Artist Parallels: Allude to iconic artists/tracks for style reference.
10. Texture: Indicate overall sound quality (e.g., "ethereal", "gritty", "lush").

Remember: Paint a sonic picture so vivid that a musician could hear the track just by reading your 120 characters. Make every word count.

Now, distill this musical vision into a precise, evocative 120-character style description:"""

    async def create_style_description(self, lyrics):
        # Check if lyrics are provided and not too short
        if not lyrics or len(lyrics) < 50:  # Arbitrary minimum length
            return "Error: Insufficient lyrics provided. Please provide complete lyrics for an accurate style description."

        # Truncate lyrics if they're too long to avoid overwhelming the AI
        max_lyrics_length = 2000  # Adjust as needed
        truncated_lyrics = lyrics[:max_lyrics_length] + ("..." if len(lyrics) > max_lyrics_length else "")

        prompt = self.prompt_template.format(lyrics=truncated_lyrics)
        response = await self.ollama.generate(prompt)
        
        # Ensure the response is within the 120-character limit
        style_description = response.strip()[:200]
        
        print("Generated style description:")
        print(style_description)
        
        return style_description

    async def refine_style_description(self, current_style, feedback):
        refine_prompt = f"""Refine this 120-character music style description based on the feedback:

Current description: {current_style}

Feedback: {feedback}

Provide an improved 120-character style description:"""

        response = await self.ollama.generate(refine_prompt)
        
        # Ensure the refined description is within the 120-character limit
        refined_style = response.strip()[:200]
        
        print("Refined style description:")
        print(refined_style)
        
        return refined_style