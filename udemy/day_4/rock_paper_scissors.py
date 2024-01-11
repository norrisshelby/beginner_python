#Let's play Rock, Paper, Scissors!

import random

print("Let's play Rock, Paper, Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]
rps = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors.\n"))

computers_choice = random.randint(0,2)

print("Rock, paper, scissors... shoot!")

print("You chose...",rps[your_choice])
print("The computer chose...",rps[computers_choice]) # another way of writing print(f"blah blah blah {blah}"")

if your_choice == computers_choice:
    print("You and the computer tied! Try again.")
elif choices[your_choice] == "rock" and choices[computers_choice] == "paper":
    print("Paper covers rock. You lose!")
elif choices[your_choice] == "rock" and choices[computers_choice] == "scissors":
    print("Rock crushes scissors. You win!")
elif choices[your_choice] == "paper" and choices[computers_choice] == "rock":
    print("Paper covers rock. You win!")
elif choices[your_choice] == "paper" and choices[computers_choice] == "scissors":
    print("Scissors cut paper. You lose!")
elif choices[your_choice] == "scissors" and choices[computers_choice] == "rock":
    print("Rock crushes scissors. You lose!")
elif choices[your_choice] == "scissors" and choices[computers_choice] == "paper":
    print("Scissors cut paper! You win!")
else:
    print("Something went wrong. Try again!")


# Rock vs. Paper (Paper wins)
# Rock vs. Scissors (Rock wins)
    
# Paper vs. Rock (Paper wins)
# Paper vs. Scissors (Scissors wins)
    
# Scissors vs. Rock (Rock wins)
# Scissors vs. Paper (Scissors wins)
    
# All others result in a tie