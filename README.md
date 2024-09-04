# 🎵 Multi-Agent Song Writing AI 🤖

Welcome to the Multi-Agent Song Writing AI project! This creative system uses multiple AI agents working together to compose original songs. It's like having a virtual band of AI musicians collaborating on your computer! 🎸🥁🎹

## 📚 Project Overview

Our AI songwriting team consists of:
- 📝 A Lyricist who crafts the words
- 🎼 A Composer who creates the melody
- 🎵 A SongWriter who coordinates the entire process

These agents use the Ollama AI model (llama3.1:latest) to generate creative content.

## 🗂️ Project Structure

- `main.py`: The entry point of our application, setting up the AI Assistant.
- `ollama.py`: Defines the Ollama class for interfacing with the Ollama API.
- `lyricist.py`: Contains the Lyricist class for generating and refining lyrics.
- `composer.py`: Houses the Composer class for creating and adjusting melodies.
- `song_writer.py`: Implements the SongWriter class to coordinate the songwriting process.
- `pyproject.toml`: Manages project dependencies and metadata using Poetry.

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
git clone https://github.com/your-username/multi-agent-song-writing-ai.git
cd multi-agent-song-writing-ai
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

Make sure to keep this running in a separate terminal window while using the song writing AI.

### Step 5: Run the Project

Activate the Poetry environment:

```bash
poetry shell
```

Then run the main script:

```bash
python main.py
```

## 🎉 Usage

When you run the main script, the AI will write a song about friendship. You can change the theme by modifying the `theme` parameter in the `assistant.write_song()` call within the `main()` function in `main.py`.

## 🔧 Customization

- To use a different Ollama model, modify the model name in the `Ollama` class instantiation in `main.py`.
- Adjust the prompts in `lyricist.py` and `composer.py` to guide the AI's creative direction.
- Modify the `SongWriter` class in `song_writer.py` to change the song creation process.

## 🤝 Contributing

We welcome contributions! If you have ideas for new features, improvements, or find any bugs, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the Ollama team for their powerful AI model
- Inspired by the creativity of human songwriters everywhere!

Happy AI-assisted songwriting! 🎶