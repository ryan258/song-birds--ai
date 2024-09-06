# File: lyricist.py

class Lyricist:
    def __init__(self, ai):
        self.ai = ai
        self.prompt_template = """Pretend you're a famous songwriter! Write a cool song about [THEME]. Your song should have:

1. A catchy title that makes people want to listen
2. Verses that tell a story or describe something
3. A chorus that repeats and is easy to remember
4. Maybe a bridge that adds something new to the song
5. An ending that wraps everything up

Use your imagination and have fun with it! Here's the theme for your song:

Theme: [THEME]

Now, write your awesome song:"""

    async def generate_lyrics(self, theme):
        # We replace [THEME] in our template with the actual theme
        prompt = self.prompt_template.replace('[THEME]', theme)
        response = await self.ai.generate(prompt)
        
        if response is None:
            print(f"Oops! We couldn't write a song about {theme} this time.")
            return None
        
        print(f"Wrote a cool song about {theme}!")
        print(f"Here's how it starts: {response[:200]}...")
        
        return response.strip()

    async def refine_lyrics(self, current_lyrics, feedback):
        refine_prompt = f"""Let's make this song even better! Here's what we have so far:

{current_lyrics}

And here's what we want to change:
{feedback}

Can you rewrite the song with these changes? Make sure to keep the whole song structure!"""

        response = await self.ai.generate(refine_prompt)
        
        if response is None:
            print("Oops! We couldn't improve the song this time.")
            return None
        
        print(f"Made the song better based on the feedback!")
        print(f"Here's how the new version starts: {response[:200]}...")
        
        return response.strip()