import random
import time

print('\n Welcome to Hangman\n')
name = input('Enter your name: ')
print('Hello ' + name)
time.sleep(2)
print('The game starts now')
time.sleep(2)

words_inplay = ['hunt', 'condense', 'paranoid', 'extraction', 'monkey', 'fierce', 'battle', 'december', 'quarantine',
                'banana', 'jazz', 'knapsack']
word = random.choice(words_inplay)
print('Guess the letters')
guesses = ''
limit = 16



while limit > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win! \n")
        print("The word is ", word)
        break

    guess = input("Guess a letter:")

    guesses += guess

    if guess not in word:
        limit -= 1
        print("Wrong")
        print("You have", +limit, "more guesses")

        if limit == 0:
            print("You Loose")
