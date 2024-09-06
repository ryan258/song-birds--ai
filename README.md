# 🎵 Song Writer AI 🤖

Welcome to Song Writer AI! This fun app helps you create songs using artificial intelligence. It's like having a robot friend who loves music and wants to write songs with you!

## 🌟 What Does It Do?

1. You give it a theme or idea for a song.
2. It writes lyrics for you.
3. It comes up with a cool music style to go with the lyrics.
4. You can make the song even better by giving it feedback.

## 🧠 How It Works

Imagine our app is like a big music factory with different rooms:

1. **The Idea Room (main.py)**
   - This is where you first enter. You tell the app what kind of song you want.
   - It's like the boss of the factory, making sure everything runs smoothly.

2. **The Lyric Writing Room (lyricist.py)**
   - Here, a super smart robot poet writes the words for your song.
   - It knows lots of words and how to make them rhyme and sound cool.

3. **The Music Style Room (composer.py)**
   - Another robot in this room thinks about what kind of music would sound good with the words.
   - It doesn't make the music, but it describes how it should sound.

4. **The Putting-It-All-Together Room (song_writer.py)**
   - This is where the lyrics and music style come together to make a complete song idea.

5. **The Talking-to-AI Room (ollama.py and openai_assistant.py)**
   - These are like telephones that let our app talk to very smart AI brains to get creative ideas.
   - You can choose which AI to use: Ollama (a local AI) or OpenAI (an online AI).

6. **The Display Room (index.html)**
   - This is where you see the finished song on your computer or phone screen.

## 🚀 How to Use It

1. Open the app in your web browser.
2. Type in an idea for a song (like "space pirates" or "friendly dragons").
3. Click the button to make a song.
4. Read the lyrics and music style the AI created.
5. If you want to make it better, give some feedback and click to refine the song.
6. You can copy the lyrics or music style description to use later.

## 📁 Important Files

- `main.py`: The main brain of the app
- `lyricist.py`: Writes the song lyrics
- `composer.py`: Comes up with the music style
- `song_writer.py`: Puts the lyrics and style together
- `ollama.py`: Talks to the Ollama AI for creative ideas
- `openai_assistant.py`: Talks to the OpenAI API for creative ideas
- `index.html`: Shows you the song on your screen

## 🛠️ Setting It Up

To make this app work on your computer, you need to:

1. Install Python (a computer language)
2. Install Poetry (helps manage the app)
3. Install Ollama (the local AI brain) - optional if you're using OpenAI
4. Get an OpenAI API key (if you want to use OpenAI instead of Ollama)

Here are the steps:

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install Poetry by following instructions at [python-poetry.org](https://python-poetry.org/docs/#installation)
3. Install Ollama from [ollama.ai](https://ollama.ai/download) (optional)
4. Clone this repository:
   ```
   git clone https://github.com/your-username/song-writer-ai.git
   cd song-writer-ai
   ```
5. Install the project dependencies:
   ```
   poetry install
   ```
6. Create a `.env` file in the project root and add your OpenAI API key (if using OpenAI):
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
7. Run the app:
   ```
   poetry run python main.py
   ```

## 🔄 Switching between Ollama and OpenAI

In `main.py`, you can change which AI the app uses:

- For Ollama: `assistant = AIAssistant("ollama")`
- For OpenAI: `assistant = AIAssistant("openai")`

Make sure you have the necessary setup (Ollama installed or OpenAI API key) for the AI you choose.

## 🎉 Have Fun!

Now you're ready to create amazing songs with your AI friend. Who knows, maybe you'll write the next big hit!

Remember, the AI is very creative, but it's your ideas that make the songs special. Happy songwriting! 🎸🎤

## 🐛 Troubleshooting

If you run into any problems:
1. Make sure all the required libraries are installed.
2. Check that your `.env` file is set up correctly if using OpenAI.
3. Ensure Ollama is running if you're using it.
4. Look at the error messages in the console for clues about what might be wrong.

If you're still stuck, ask a grown-up or teacher for help!