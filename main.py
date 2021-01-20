import random
from wordlist import generate_word_list
from guess import guess

lives = 6

# Generate a random number to get a
# random word from the list
random.seed()
random_word = random.randint(0, 29)
word = (generate_word_list()[random_word]).lower()

guess_letter_position = list('_'*len(word))

print(" ".join(guess_letter_position))

# Get a guess from the user

# Check the guess
while (lives > 0):
    guess_letter = (input("Guess a letter --> ")).lower()
    if guess(guess_letter, word):
        position = word.find(guess_letter)

        for i in range(len(word)):
            guess_letter_position[position] = guess_letter
            if position < word.find(guess_letter, position+1):
                position = word.find(guess_letter, position+1)

        print(" ".join(guess_letter_position))
    else:
        lives -= 1
        print(" ".join(guess_letter_position))
        if lives > 1:
            print("Only {} lives left".format(lives))
        elif lives == 1:
            print("Only {} life left".format(lives))
        else:
            print("Game Over! The word was: {}".format(word))
            break
    if "".join(guess_letter_position) == word:
        print("Congratulations!!")
        break
