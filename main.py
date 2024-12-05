import os
from art import logo
import random

print(logo)
print("Welcome to Number Guessing Game!")

def think_number():
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)


def guess(attempts):
    thought_number = think_number()
    attempts_remaining = attempts
    while attempts_remaining > 0:
        guess = input("Make a guess: ")
        if int(guess) == thought_number:
            print(f"You got it! The answer was {thought_number}.")
            break
        elif int(guess) < thought_number:
            print("Too low.")
            print("Guess again.")
            attempts_remaining -= 1
            print(f"You have {attempts_remaining} attempts remaining.")
        elif int(guess) > thought_number:
            print("Too high.")
            print("Guess again.")
            attempts_remaining -= 1
            print(f"You have {attempts_remaining} attempts remaining.")
        else:
            print("That's not a number.")

def game():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess(attempts)
    elif level == "hard":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess(attempts)

while True:
    game()
    play_again = input("Would you like to play again? (Y/N): ").lower()
    os.system('cls')
    print(logo)
    print("Welcome to Number Guessing Game!")
    if play_again != 'y':
        print("Thanks for playing!")
        break