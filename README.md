# Hangman Game

A fun and interactive Hangman game built using Python's Tkinter library. The game includes multiple difficulty levels, a hint system, lives and score tracking, and integrates with the [DictionaryAPI.dev](https://dictionaryapi.dev/) to provide real word definitions as clues!

## 🎮 Features

- ✅ GUI built with Tkinter
- ✅ Easy, Medium, and Hard difficulty levels
- ✅ Word categories loaded from a separate `words.py` file
- ✅ Visual ASCII hangman states
- ✅ Scoring system
- ✅ Lives counter
- ✅ Hint system with 3 hint types:
  - Reveal first letter
  - Reveal a random letter
  - Provide a dictionary definition (via API)
- ✅ Error handling for invalid inputs
- ✅ Game restarts after win or loss

## 🧠 Hints

Players can choose from 3 hint types:
1. **First Letter** – Reveals the starting letter of the word.
2. **Random Letter** – Reveals a random letter (excluding the first).
3. **Definition** – Provides a clue/definition from [DictionaryAPI.dev](https://dictionaryapi.dev/).

Each hint can only be used once per game.

## 📦 Project Structure
Hangman-Game/ ├── main.py # Main game logic and GUI
              ├── words.py # Dictionary of categorized word lists 
              ├── README.md # Project overview 
              └── requirements.txt


## 🛠 Requirements

- Python 3.6+
- Tkinter (usually pre-installed)
- `requests` library

Install dependencies:

```bash
pip install requests
```

## 🚀 How to Run
```bash
python3 main.py
```
