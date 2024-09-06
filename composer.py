# File: composer.py

class Composer:
    def __init__(self, ai):
        self.ai = ai
        self.prompt_template = """Imagine you're a super cool music producer! You need to come up with an awesome music style for these song lyrics:

{lyrics}

Think about:

1. What kind of music it should be (like pop, rock, hip-hop, etc.)
2. What instruments would sound good
3. How fast or slow the song should be
4. If the song should be happy, sad, or somewhere in between
5. Any special sound effects that might be fun to add

Now, describe the perfect music style for this song in about 120 letters or less. Make it sound exciting!"""

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
        refine_prompt = f"""Let's make the music style even cooler! Here's what we have now:

Current style: {current_style}

And here's how we want to change it:
{feedback}

Can you describe a new and improved music style in about 120 letters?"""

        response = await self.ai.generate(refine_prompt)
        
        # Make sure our new description isn't too long
        refined_style = response.strip()[:200]
        
        print("Made the music style even better:")
        print(refined_style)
        
        return refined_style