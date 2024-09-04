# 🎼 File: composer.py 🎼

class Composer:
    def __init__(self, ollama):
        # 🤖 Our AI model
        self.ollama = ollama

    async def create_melody(self, lyrics):
        # 🎵 Ask our AI to describe a melody
        prompt = f"Create a simple melody description for these lyrics:\n\n{lyrics}\n\nDescribe the melody in terms of pitch and rhythm."
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        melody = response.strip()
        
        print("🎶 Melody is composed!")
        return melody

    async def adjust_melody(self, melody, feedback):
        # 🔧 Improve the melody based on feedback
        prompt = f"Adjust this melody based on the feedback:\n\nMelody:\n{melody}\n\nFeedback:{feedback}"
        response = await self.ollama.generate(prompt)  # Use the generate method
        
        adjusted_melody = response.strip()
        
        print("🎵 Melody has been fine-tuned!")
        return adjusted_melody