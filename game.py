# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

#Prompt User for input

#x = input("Choose 'rock' or 'paper' or scissor'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print(user_choice)

# Computer Choice (At Random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("User Chose This")
print(user_choice)
print("Computer Chose This")
print(computer_choice)