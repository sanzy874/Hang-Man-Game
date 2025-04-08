# 🪓 Hangman Game in Python

This is a fun and interactive Hangman game built in Python, featuring both:

- **Graphical User Interface (GUI)** version built with `Tkinter`
- **Terminal-based** version for CLI lovers

---

## 📁 Project Structure

- `main` branch → **GUI version** with hint system, scoring, lives, and dictionary API integration.
- `terminal-version` branch → **Classic terminal version** with difficulty levels and ASCII hangman.

---

## 🚀 Features (GUI Version)

✅ Choose from Easy, Medium, or Hard difficulty  
✅ Hint system with options:  
  - First letter  
  - Random unrevealed letter  
  - Word definition from [DictionaryAPI.dev](https://dictionaryapi.dev)  
✅ Score tracking  
✅ Remaining lives shown  
✅ ASCII art for hangman  
✅ Clean and responsive GUI using Tkinter  
✅ Error handling and validations  

---

## 🧩 Getting Started

### 🔧 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

### 🎮 Run the Game
## GUI Version (Tkinter)
```bash
python main.py
```
## Terminal Version
Switch to the terminal-version branch:
```bash
git checkout terminal-version
python terminal_game.py
```

## 🧠 Hint System (GUI)

You can click the **Hint** button and choose from:

- Reveal the **first letter**
- Reveal a **random unrevealed letter**
- Get the word’s **definition** using [DictionaryAPI.dev](https://dictionaryapi.dev)

⚠️ **Each hint can only be used once per game.**

---

## 🛠 Development

### Branches

- `main` – GUI with Tkinter and hint system  
- `terminal-version` – Classic command-line hangman

---

## 🤝 Contributions

Pull requests and suggestions are welcome!  
