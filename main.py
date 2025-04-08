import random
import tkinter as tk
from tkinter import messagebox
from words import WORDS  # Import the word lists from the new file

# ASCII art for hangman states.
HANGMANPICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.difficulty = tk.StringVar(value="easy")
        self.setup_difficulty_screen()

    def setup_difficulty_screen(self):
        # Screen to select difficulty level.
        self.clear_screen()
        label = tk.Label(self.master, text="Choose difficulty:", font=("Helvetica", 14))
        label.pack(pady=10)
        
        for level in WORDS.keys():
            rb = tk.Radiobutton(self.master, text=level.capitalize(), variable=self.difficulty, value=level, font=("Helvetica", 12))
            rb.pack(anchor="w")
        
        start_btn = tk.Button(self.master, text="Start Game", command=self.start_game, font=("Helvetica", 12))
        start_btn.pack(pady=20)

    def start_game(self):
        self.secret_word = random.choice(WORDS[self.difficulty.get()])
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = len(HANGMANPICS) - 1
        
        self.clear_screen()
        # Create labels and entry for game play.
        self.hangman_label = tk.Label(self.master, text=HANGMANPICS[self.wrong_guesses], font=("Courier", 12), justify="left")
        self.hangman_label.pack(pady=10)
        
        self.word_label = tk.Label(self.master, text=self.get_display_word(), font=("Helvetica", 16))
        self.word_label.pack(pady=10)
        
        self.entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=5)
        self.entry.focus_set()
        
        submit_btn = tk.Button(self.master, text="Guess", command=self.process_guess, font=("Helvetica", 12))
        submit_btn.pack(pady=5)

    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.secret_word)

    def process_guess(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showinfo("Invalid Input", "Please enter a single alphabetical character.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You have already guessed '{guess}'.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess not in self.secret_word:
            self.wrong_guesses += 1
        
        # Update GUI components.
        self.hangman_label.config(text=HANGMANPICS[self.wrong_guesses])
        self.word_label.config(text=self.get_display_word())
        
        # Check win/loss conditions.
        if all(letter in self.guessed_letters for letter in self.secret_word):
            messagebox.showinfo("Congratulations!", f"You've guessed it! The word was '{self.secret_word.upper()}'.")
            self.setup_difficulty_screen()
        elif self.wrong_guesses >= self.max_wrong:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{self.secret_word.upper()}'.")
            self.setup_difficulty_screen()

    def clear_screen(self):
        # Remove all widgets from the master window.
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
