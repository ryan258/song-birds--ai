# File: composer.py

class Composer:
    def __init__(self, ai):
        self.ai = ai
        self.prompt_template = """Embody the role of a visionary music producer with a keen ear for innovative sounds and emotionally resonant compositions. Your mission is to craft the perfect musical style for the following lyrics:

{lyrics}

In your creative process, consider:

1. Genre fusion: Blend multiple genres to create a unique sound that complements the lyrics
2. Instrumentation: Choose instruments that enhance the emotional tone and message of the song
3. Rhythm and tempo: Determine the ideal pace and rhythmic patterns to support the narrative flow
4. Mood and atmosphere: Develop a sonic landscape that amplifies the emotional core of the lyrics
5. Production techniques: Incorporate innovative studio effects or recording methods to add depth

Additional factors to elevate your production:

- Dynamic shifts: Plan moments of intensity and quietude to create an engaging listening experience
- Textural layers: Consider how different sonic elements can be layered to create richness and complexity
- Cultural influences: Draw inspiration from diverse musical traditions to add unique flavors
- Vocal treatment: Suggest approaches for vocal delivery and harmonies that complement the style
- Memorable hooks: Identify opportunities for musical motifs that will stick in listeners' minds

Now, in approximately 120 letters, describe your groundbreaking musical style for this song. Paint a vivid picture of how it will sound and feel, exciting the imagination of anyone who reads it:"""

    async def create_style_description(self, lyrics):
        # Check if we have enough lyrics to work with
        if not lyrics or len(lyrics) < 50:
            return "Oops! We need more lyrics to come up with a good music style. Can you write a bit more?"

        # If the lyrics are too long, we'll just use the first part
        max_lyrics_length = 2000
        short_lyrics = lyrics[:max_lyrics_length] + ("..." if len(lyrics) > max_lyrics_length else "")

        prompt = self.prompt_template.format(lyrics=short_lyrics)
        response = await self.ai.generate(prompt)
        
        # Make sure our description isn't too long
        style_description = response.strip()[:200]
        
        print("Created an awesome music style:")
        print(style_description)
        
        return style_description

    async def refine_style_description(self, current_style, feedback):
        refine_prompt = f"""As our visionary music producer, your task is to evolve this musical style into something truly extraordinary. Here's our current style:

Current style: {current_style}

We've received the following feedback for improvement:
{feedback}

Your mission:
1. Analyze the current style and the feedback critically.
2. Incorporate the suggested changes while maintaining the essence of the original concept.
3. Push the boundaries of creativity - consider unexpected genre fusions, innovative instrumentation, or cutting-edge production techniques.
4. Ensure the refined style complements and elevates the song's lyrics and emotional core.
5. Paint a vivid sonic picture that excites the imagination and emotionally resonates with listeners.

In approximately 120 words, describe the evolved musical style. Make it so compelling that anyone reading it can almost hear the groundbreaking sound you've crafted."""

        response = await self.ai.generate(refine_prompt)
        
        # Make sure our new description isn't too long
        refined_style = response.strip()[:200]
        
        print("Made the music style even better:")
        print(refined_style)
        
        return refined_style