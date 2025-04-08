import random

# ANSI escape codes for colors
GREEN = "\033[92m"   # correct letter in correct position
YELLOW = "\033[93m"  # letter exists in word but in wrong position
GREY = "\033[90m"    # letter not in word
RESET = "\033[0m"    # resets the color

def choose_word():
    # A list of valid five-letter words.
    words = [
        "apple", "brave", "crane", "dance", "eagle", 
        "flame", "ghost", "hotel", "input", "joker"
    ]
    return random.choice(words)

def evaluate_guess(secret, guess):
    """Compares guess to secret and returns a list of colored letters."""
    result = [''] * len(secret)
    secret_chars = list(secret)
    
    # First pass: Check letters in the correct position.
    for i, (s_char, g_char) in enumerate(zip(secret, guess)):
        if g_char == s_char:
            result[i] = GREEN + g_char.upper() + RESET
            secret_chars[i] = None  # Remove correctly matched letters

    # Second pass: Check letters that exist in the word in the wrong position.
    for i, g_char in enumerate(guess):
        if result[i] != '':  # Skip already correctly matched letters.
            continue
        if g_char in secret_chars:
            result[i] = YELLOW + g_char.upper() + RESET
            # Remove the matched letter to avoid duplicate matching.
            secret_chars[secret_chars.index(g_char)] = None
        else:
            result[i] = GREY + g_char.upper() + RESET

    return " ".join(result)

def wordle():
    secret_word = choose_word()
    word_length = len(secret_word)
    attempts = 6

    print("Welcome to Wordle!")
    print(f"Guess the {word_length}-letter word. You have {attempts} attempts.\n")

    for attempt in range(1, attempts+1):
        guess = input(f"Attempt {attempt}: ").lower().strip()

        # Validate the guess length.
        if len(guess) != word_length:
            print(f"Please enter a {word_length}-letter word.\n")
            continue

        # Evaluate the guess and output colored feedback.
        feedback = evaluate_guess(secret_word, guess)
        print(feedback + "\n")

        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"Sorry, you're out of attempts. The word was '{secret_word.upper()}'.")

if __name__ == "__main__":
    wordle()
