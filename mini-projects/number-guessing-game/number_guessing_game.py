#Guessing Game
import random
def play_game():
    number = random.randint(1, 1000)
    guess = int(input("Guess the number: "))
    attempts = 0
    while guess != number:
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        guess = int(input("Guess the number: "))
    attempts += 1
    print("Correct!")
    if attempts == 1:
        print(f"You got it after {attempts} guess")
    else:
        print(f"You got it after {attempts} guesses")

play_game()
