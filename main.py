"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Adéla Pečená
email: adela.pecena@email.cz
discord: Adéla Pečená#5431
"""

import random

def generate_secret_number():
    """Generuje náhodné 4 místné číslo s unikátními číslicemi."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def validate_guess(guess, secret):
    """Validuje hádání uživatele."""
    if len(guess) != 4 or not guess.isdigit() or guess[0] == '0' or len(set(guess)) != 4:
        return False
    return True

def evaluate_guess(guess, secret):
    """Ohodnotí hádání uživatele."""
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    """Hlavní funkce pro hraní hry."""
    secret_number = generate_secret_number()
    guesses = 0

    print("Hi there!\n-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    while True:
        user_input = input("Enter a number: ")

        if not validate_guess(user_input, secret_number):
            print("Invalid input. Please enter a 4-digit number with unique digits (not starting with 0).")
            continue

        bulls, cows = evaluate_guess(user_input, secret_number)
        guesses += 1

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            break
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

if __name__ == "__main__":
    play_game()
