import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right." ')
first_choice = first_choice.lower()


if first_choice == "right":
    print("Oops! Sorry! You fell into a hole. Game over!")
    sys.exit()
    
else: 
    print("You survived. You might not be so lucky next time. Your next choice awaits you!")


second_choice = input("Do you wish to push your luck by crossing a deadly sea to land, or wait on shore for a boat? If you wish"
                      " to cross, type 's' for swim. If go by boat, type 'b'. ")

if second_choice == "s":
    print(":( You decided to swim and you were attacked by trout. Game over!")
    sys.exit()

else:
    print("You made the smart choice to wait for a boat. Will you survive what's behind the next door?")