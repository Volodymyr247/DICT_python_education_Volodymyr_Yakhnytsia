print("Hangman")
print("The game will be available soon.")
print("Hangman")
word = input("Guess the word: > ")
if word == "python":
    print("You survived!")
else:
    print("You lost!")
import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
print("Hangman")
guess = input("Guess the word: > ")
if guess == secret_word:
    print("You survived!")
else:
  print("You lost!")
import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
hint = secret_word[:3] + "-" * (len(secret_word) - 3)
print("Hangman")
guess = input(f"Guess the word {hint}: > ")
if guess == secret_word:
    print("You survived!")
else:
    print("You lost!")
import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_letters = set()
print("Hangman")
for _ in range(8):
    print()
    display = "".join([char if char in guessed_letters else "-" for char in secret_word])
    print(display)
    letter = input("Input a letter: > ")
    if letter in secret_word:
        guessed_letters.add(letter)
    else:
        print("That letter doesn't appear in the word")
print("Thanks for playing!")
print("We'll see how well you did in the next stage")
import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_letters = set()
lives = 8
print("Hangman")
while lives > 0:
    print()
    display = "".join([char if char in guessed_letters else "-" for char in secret_word])
    print(display)
    if "-" not in display:
        print("You guessed the word!")
        print("You survived!")
        break
    letter = input("Input a letter: > ")
    if letter in secret_word:
        if letter in guessed_letters:
            print("No improvements")
            lives -= 1
        else:
            guessed_letters.add(letter)
    else:
         print("That letter doesn't appear in the word")
         lives -= 1
else:
    print("You lost!")
import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_letters = set()
lives = 8
print("Hangman")
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
        print("You already guessed this letter!")
        continue
    guessed_letters.add(letter)
    if letter not in secret_word:
        print("That letter doesn't appear in the word")
        lives -= 1
    else:
        print("You lost!")
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
        if letter in guessed_letters:
            print("You already guessed this letter!")
            continue
        guessed_letters.add(letter)
        if letter not in secret_word:
            print("That letter doesn't appear in the word")
            lives -= 1
    else:
        print("You lost!")
def main():
    print("Hangman")
    while True:
        action = input('Type "play" to play the game, "exit" to quit: > ')
        if action == "play":
            play_game()
        elif action == "exit":
            break
if __name__ == "__main__":
    main()























