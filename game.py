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

if ((computer_choice == rock) and (user_choice == scissor))
print("Computer Wins!")
if ((computer_choice == paper) and (user_choice == scissor))
print("You Win!")
if ((computer_choice == scissor) and (user_choice == scissor))
print("Tie!")

if ((computer_choice == rock) and (user_choice == rock))
print("Tie!")
if ((computer_choice == paper) and (user_choice == rock))
print("Computer Wins!")
if ((computer_choice == scissor) and (user_choice == rock))
print("You Win!")

if ((computer_choice == rock) and (user_choice == paper))
print("You Win!")
if ((computer_choice == paper) and (user_choice == paper))
print("Tie!")
if ((computer_choice == scissor) and (user_choice == paper))
print("Computer Wins!")