import random

def choose_word():
    words = ["python", "hangman", "diamond", "developer", "notebook"]
    return random.choice(words)

def display_word(word, guessed_letters):
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

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou guessed it! The word was '{word}'. You win! 🎉")
            return

    print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
