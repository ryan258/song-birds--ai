# 📝 File: lyricist.py 📝

class Lyricist:
    def __init__(self, ollama):
        # 🤖 Our AI model
        self.ollama = ollama

    async def generate_lyrics(self, theme):
        # 💡 Ask our AI to write lyrics
        prompt = f"Write lyrics for a song about {theme}. Make it 2 verses and a chorus."
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        # ✨ Clean up the lyrics
        lyrics = response.strip()
        
        print("✏️ Lyrics are ready!")
        return lyrics

    async def refine_lyrics(self, lyrics, feedback):
        # 🔧 Improve the lyrics based on feedback
        prompt = f"Refine these lyrics based on the feedback:\n\nLyrics:\n{lyrics}\n\nFeedback:{feedback}"
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        refined_lyrics = response.strip()
        
        print("🎨 Lyrics have been polished!")
        return refined_lyrics