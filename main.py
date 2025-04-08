import random

# Hangman ASCII art for 0 to 6 wrong guesses.
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

# Word lists by difficulty level.
WORDS = {
    "easy": ["apple", "bread", "candy", "dream", "flame"],
    "medium": ["python", "hangman", "jungle", "puzzle", "quartz"],
    "hard": ["awkward", "rhythms", "cryptic", "zephyr", "mnemonic"]
}

def choose_word(difficulty):
    return random.choice(WORDS[difficulty])

def display_word(secret, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret)

def terminal_hangman():
    print("Welcome to Hangman!")
    difficulty = ""
    while difficulty not in WORDS:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower().strip()
        if difficulty not in WORDS:
            print("Invalid choice. Please choose easy, medium, or hard.")

    secret_word = choose_word(difficulty)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMANPICS) - 1

    while wrong_guesses < max_wrong:
        # Display ASCII art and the current known letters.
        print(HANGMANPICS[wrong_guesses])
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.\n")
            continue

        guessed_letters.add(guess)
        if guess in secret_word:
            print("Good guess!\n")
            # Check if the full word has been revealed.
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You've guessed the word:", secret_word.upper())
                return
        else:
            print("Wrong guess.\n")
            wrong_guesses += 1

    # Out of tries – game over
    print(HANGMANPICS[wrong_guesses])
    print("Game over! The word was:", secret_word.upper())

if __name__ == "__main__":
    terminal_hangman()
