import random

def choose_word():
    words = ["python", "hangman", "diamond", "developer", "notebook"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Reveal letters that have been guessed; otherwise, display an underscore
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        # Make sure the player enters exactly one alphabetical letter.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # Check if the letter was already guessed.
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # If the guess is in the word, update guessed_letters; otherwise, deduct a try.
        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess.")
        
        # Check if every letter in the word has been guessed correctly.
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou guessed it! The word was '{word}'. You win! 🎉")
            break
    else:
        print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
