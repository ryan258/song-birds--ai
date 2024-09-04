# 🎵 Song Writer AI 🤖

Welcome to the Song Writer AI project! This creative system uses multiple AI agents working together to compose original songs. It's like having a virtual band of AI musicians collaborating on your computer!

## 📚 Project Overview

Our AI songwriting team consists of:
- 📝 A Lyricist who crafts the words
- 🎼 A Composer who creates the melody
- 🎵 A SongWriter who coordinates the entire process

These agents use the Ollama AI model to generate creative content.

## 🎨 Features

- Generate initial song drafts based on user-provided themes
- Refine lyrics and melodies iteratively
- Display song drafts in reverse chronological order
- Copy lyrics and melodies to clipboard with a single click

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Poetry (for managing dependencies)
- Ollama (for running the AI model)

### Step 1: Install Poetry

If you don't have Poetry installed, you can get it by running:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/song-writer-ai.git
cd song-writer-ai
```

### Step 3: Install Dependencies

In the project directory, run:

```bash
poetry install
```

This will create a virtual environment and install all the necessary dependencies.

### Step 4: Install and Run Ollama

1. Follow the instructions on the [Ollama website](https://ollama.ai/) to install Ollama on your system.
2. Once installed, run the Llama 3.1 model:

```bash
ollama run llama3.1:latest
```

Make sure to keep this running in a separate terminal window while using the Song Writer AI.

## 🚀 Usage

1. Start the application:

```bash
poetry run python main.py
```

2. Open a web browser and go to `http://localhost:5000`.

3. Enter a theme for your song and click "Write Initial Draft".

4. Once the initial draft is generated, you can refine the song by entering instructions for lyrics refinement and melody adjustment.

5. Click "Refine Song" to generate a new version based on your instructions.

6. You can continue refining the song multiple times, with each new version appearing at the top of the page.

7. Use the "Copy Lyrics" and "Copy Melody" buttons to easily copy parts of your song to the clipboard.

## 📝 Project Structure

- `main.py`: The entry point of our application, setting up the AI Assistant and Flask server.
- `ollama.py`: Defines the Ollama class for interfacing with the Ollama API.
- `lyricist.py`: Contains the Lyricist class for generating and refining lyrics.
- `composer.py`: Houses the Composer class for creating and adjusting melodies.
- `song_writer.py`: Implements the SongWriter class to coordinate the songwriting process.
- `frontend/index.html`: The web interface for interacting with the Song Writer AI.

## 🤝 Contributing

We welcome contributions! If you have ideas for new features, improvements, or find any bugs, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the Ollama team for their powerful AI model
- Inspired by the creativity of human songwriters everywhere!

Happy AI-assisted songwriting! 🎶