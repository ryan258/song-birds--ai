# File: lyricist.py

class Lyricist:
    def __init__(self, ai):
        self.ai = ai
        self.prompt_template = """You are a world-renowned songwriter with a unique ability to capture emotions and tell compelling stories through your lyrics. Your task is to create an extraordinary song based on the theme: [THEME].

Your song should include:

1. An attention-grabbing title that encapsulates the essence of the song
2. Verses that weave a narrative or paint vivid imagery, using metaphors and sensory details
3. A memorable chorus with a powerful hook that resonates emotionally
4. A bridge that adds depth or offers a new perspective on the theme
5. A satisfying conclusion that ties the song's elements together

Consider the following to elevate your songwriting:

- Employ varied rhyme schemes and rhythmic patterns to add complexity
- Use literary devices such as alliteration, assonance, or personification
- Incorporate unexpected twists or moments of revelation
- Balance specificity and universality to make the song relatable yet unique
- Consider the emotional journey of the listener throughout the song

Theme: [THEME]

Now, channel your creativity and craft a song that will move hearts and minds:"""

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
        refine_prompt = f"""As our expert songwriter, your task is to elevate this song to new heights of creativity and emotional impact. Here's our current version:

{current_lyrics}

We've received the following feedback for improvement:
{feedback}

Your mission:
1. Carefully analyze the feedback and the current lyrics.
2. Implement the suggested changes while preserving the song's core message and emotional resonance.
3. Take creative liberty to enhance other aspects of the song that complement the requested changes.
4. Ensure the refined lyrics maintain or improve upon the song's structure, flow, and coherence.
5. Aim to surprise and delight with unexpected twists or deeper emotional connections.

Please provide the refined version of the entire song, showcasing your mastery in songwriting and your ability to transform feedback into lyrical gold."""

        response = await self.ai.generate(refine_prompt)
        
        if response is None:
            print("Oops! We couldn't improve the song this time.")
            return None
        
        print(f"Made the song better based on the feedback!")
        print(f"Here's how the new version starts: {response[:200]}...")
        
        return response.strip()