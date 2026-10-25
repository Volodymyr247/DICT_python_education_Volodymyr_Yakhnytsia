import random

def play_game():
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    guessed_letters = set()
    lives = 8

    while lives > 0:
        print()
        display = "".join([char if char in guessed_letters else "-" for char in secret_word])
        print(display)

        if "-" not in display:
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            break

        letter = input("Input a letter: > ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not (letter.islower() and letter.isalpha() and letter.isascii()):
            print("Please enter a lowercase English letter")
            continue

        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(letter)

        if letter not in secret_word:
            print("That letter doesn't appear in the word")
            lives -= 1
    else:
        print("You lost!")

def main():
    print("HANGMAN")
    while True:
        action = input('Type "play" to play the game, "exit" to quit: > ')
        if action == "play":
            play_game()
        elif action == "exit":
            break

if __name__ == "__main__":
    main()