import os

class Lyricist:
    def __init__(self, ollama):
        self.ollama = ollama
        self.prompt_template = """Embody the spirit of a legendary songwriter to craft a profound and memorable song about [THEME]. Your creation should:

1. Title: Forge an intriguing, theme-resonant title that hooks the listener.

2. Structure:
   - Verse 1: Set the scene, introduce the core concept
   - Chorus: Distill the song's essence, make it unforgettable
   - Verse 2: Deepen the narrative, add layers to the theme
   - Chorus: Repeat, allowing for slight variations if fitting
   - Bridge: Offer a new perspective or twist
   - Final Chorus: Deliver with heightened emotional impact

3. Lyrical Craftsmanship:
   - Employ vivid imagery and powerful metaphors
   - Weave in clever wordplay and double meanings
   - Use alliteration, assonance, and internal rhymes thoughtfully
   - Vary line lengths and rhythms for dynamic flow

4. Emotional Journey:
   - Begin with a compelling hook or thought-provoking line
   - Build emotional intensity throughout
   - Culminate in a powerful, resonant ending

5. Thematic Depth:
   - Explore [THEME] from multiple angles
   - Layer in subtext and deeper meanings
   - Maintain thematic consistency while avoiding clichés

6. Musical Considerations:
   - Craft lyrics that lend themselves to melodic interpretation
   - Consider potential for dynamic vocal delivery
   - Leave room for instrumental sections where appropriate

7. Universal Appeal:
   - Balance specific details with universal emotions
   - Create lines that invite personal interpretation

Remember: Your lyrics should tell a story, evoke strong emotions, and leave a lasting impact. They should read like poetry and sing like a hit.

Theme: [THEME]

Now, channel the muses and provide your complete, section-labeled masterpiece:
"""

    async def generate_lyrics(self, theme):
        # Use str.replace() for safe interpolation
        prompt = self.prompt_template.replace('[THEME]', theme)
        response = await self.ollama.generate(prompt)
        
        print(f"Generated complete lyrics for theme: {theme}")
        print(f"First 200 characters: {response[:200]}...")
        
        return response.strip()

    async def refine_lyrics(self, current_lyrics, feedback):
        refine_prompt = f"""Refine the following lyrics based on this feedback. Maintain the complete song structure:

Current lyrics:
{current_lyrics}

Feedback:
{feedback}

Please provide the complete refined lyrics:"""

        response = await self.ollama.generate(refine_prompt)
        
        print(f"Refined lyrics based on feedback")
        print(f"First 200 characters of refined lyrics: {response[:200]}...")
        
        return response.strip()