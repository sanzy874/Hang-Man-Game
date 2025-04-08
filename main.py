import random
import requests
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

def fetch_definition(word):
    """
    Fetches a definition for the given word from DictionaryAPI.dev.
    If successful, returns the first available definition.
    Otherwise, returns a default message.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Attempt to retrieve the first definition from the first meaning.
            definition = data[0]["meanings"][0]["definitions"][0]["definition"]
            return definition
        else:
            return "Definition not available."
    except Exception as e:
        return "Definition not available."

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.score = 0  # Initialize a score counter.
        self.difficulty = tk.StringVar(value="easy")
        self.setup_difficulty_screen()
    
    def setup_difficulty_screen(self):
        self.clear_screen()
        title = tk.Label(self.master, text="Choose Difficulty", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)
        
        for level in WORDS.keys():
            rb = tk.Radiobutton(self.master, text=level.capitalize(), variable=self.difficulty, value=level, font=("Helvetica", 12))
            rb.pack(anchor="w", padx=20)
        
        start_btn = tk.Button(self.master, text="Start Game", command=self.start_game, font=("Helvetica", 12))
        start_btn.pack(pady=20)
    
    def start_game(self):
        self.secret_word = random.choice(WORDS[self.difficulty.get()])
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = len(HANGMANPICS) - 1
        self.hint_used = 0
        
        self.clear_screen()
        
        # Create a status frame for lives and score.
        status_frame = tk.Frame(self.master)
        status_frame.pack(pady=5)
        self.lives_label = tk.Label(status_frame, text="", font=("Helvetica", 12))
        self.lives_label.pack(side=tk.LEFT, padx=10)
        self.score_label = tk.Label(status_frame, text=f"Score: {self.score}", font=("Helvetica", 12))
        self.score_label.pack(side=tk.LEFT, padx=10)
        self.update_status()  # Update lives remaining
        
        # Hangman display.
        self.hangman_label = tk.Label(self.master, text=HANGMANPICS[self.wrong_guesses], font=("Courier", 12), justify="left")
        self.hangman_label.pack(pady=10)
        
        # Word display.
        self.word_label = tk.Label(self.master, text=self.get_display_word(), font=("Helvetica", 16))
        self.word_label.pack(pady=10)
        
        # Entry and guess button.
        entry_frame = tk.Frame(self.master)
        entry_frame.pack(pady=5)
        self.entry = tk.Entry(entry_frame, font=("Helvetica", 14))
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.focus_set()
        guess_btn = tk.Button(entry_frame, text="Guess", command=self.process_guess, font=("Helvetica", 12))
        guess_btn.pack(side=tk.LEFT, padx=5)
        
        # Hint button.
        hint_btn = tk.Button(self.master, text="Hint", command=self.give_hint, font=("Helvetica", 12))
        hint_btn.pack(pady=5)
    
    def update_status(self):
        lives_remaining = self.max_wrong - self.wrong_guesses
        self.lives_label.config(text=f"Lives: {lives_remaining}")
        self.score_label.config(text=f"Score: {self.score}")
    
    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.secret_word)
    
    def process_guess(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showinfo("Invalid Input", "Please enter a single alphabetical character.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You've already guessed '{guess}'.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess not in self.secret_word:
            self.wrong_guesses += 1
        
        # Update the hangman drawing and displayed word.
        self.hangman_label.config(text=HANGMANPICS[self.wrong_guesses])
        self.word_label.config(text=self.get_display_word())
        self.update_status()
        
        # Check win condition.
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.score += 1  # Increase score on win.
            messagebox.showinfo("Congratulations!", f"You've guessed the word '{self.secret_word.upper()}'!\nYour score is now {self.score}.")
            self.setup_difficulty_screen()
        # Check loss condition.
        elif self.wrong_guesses >= self.max_wrong:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{self.secret_word.upper()}'.")
            self.setup_difficulty_screen()
    
    def give_hint(self):
        if self.hint_used >= 3:
            messagebox.showinfo("Hint", "You've used all your hints!")
            return

        self.hint_used += 1

        if self.hint_used == 1:
            hint = f"The word starts with '{self.secret_word[0].upper()}'."
        elif self.hint_used == 2:
            unrevealed_letters = list(set(self.secret_word[1:]))  # Exclude first letter to avoid repetition
            random_letter = random.choice(unrevealed_letters)
            hint = f"One of the letters is '{random_letter.upper()}'."
        elif self.hint_used == 3:
            definition = fetch_definition(self.secret_word)
            hint = f"Clue: {definition}"

        messagebox.showinfo(f"Hint #{self.hint_used}", hint)

    def clear_screen(self):
        # Remove all widgets in the main window.
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()