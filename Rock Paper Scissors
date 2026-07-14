import random
def game():
    selection = ["rock", "paper", "scissors"]
    computer = random.choice(selection)
    user = input("rock, paper or scissors: ")
    def com_choice():
        print(f"computer chose {computer}")
    def gameplay():
        if user == "rock" and computer == "paper":
            print ("Computer wins!")
            com_choice()
        elif user == "paper" and computer == "rock":
            print ("You win!")
            com_choice()
        elif user == "rock" and computer == "scissors":
            print ("You win!")
            com_choice()
        elif user == "scissors" and computer == "rock":
            print ("Computer wins!")
            com_choice()
        elif user == "paper" and computer == "scissors":
            print ("Computer wins!")
            com_choice()
        elif user == "scissors" and computer == "paper":
            print ("You win!")
            com_choice()
        elif user == computer:
            print ("Draw, Try again?")
            com_choice()
        else:
            print("Pick between 'rock', 'paper', and 'scissors'")
            return
        if user not in ["rock", "paper", "scissors"]:
            return
        playing = True
        while playing:
            game()
            again = input(f"Try again? Yes or NO: ")
            if again.lower() != "yes":
                playing = False
                print("End!")
    gameplay()
def begin():
    start = input("Ready to play, Yes or No?: ")
    if start == "Yes" or start == "yes":
        game()
    else:
        print("End!")
begin()