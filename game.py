# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

#Prompt User for input

#x = input("Choose 'rock' or 'paper' or scissor'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")

# Computer Choice (At Random)

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("NOT VALID OPTION")
    exit()

computer_choice = random.choice(options)
print("User Chose This")
print(user_choice)
print("Computer Chose This")
print(computer_choice)

if (computer_choice == "rock") and (user_choice == "scissors"):
    print("Computer Wins!")
elif (computer_choice == "paper") and (user_choice == "scissors"):
    print("You Win!")
elif (computer_choice == "scissors") and (user_choice == "scissors"):
    print("Tie!")
elif (computer_choice == "rock") and (user_choice == "rock"):
    print("Tie!")
elif (computer_choice == "paper") and (user_choice == "rock"):
    print("Computer Wins!")
elif (computer_choice == "scissors") and (user_choice == "rock"):
    print("You Win!")
elif (computer_choice == "rock") and (user_choice == "paper"):
    print("You Win!")
elif (computer_choice == "paper") and (user_choice == "paper"):
    print("Tie!")
elif (computer_choice == "scissors") and (user_choice == "paper"):
    print("Computer Wins!")

print("Thanks for Playing!")