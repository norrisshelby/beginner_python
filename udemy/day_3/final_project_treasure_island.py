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

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right."\n').lower()

if choice1 == "left":
#continue the game
    print("You survived. You might not be so lucky next time. Your next choice awaits you!")
    print("""   ,--.     ,--.
 (  O )   (  O )
  `--'  \  `--'
         \   _
   >-.   /   /| 
      `-.__.' """)
    choice2 = input("Do you wish to push your luck by crossing a deadly sea to land, or wait on shore for a boat? If you wish"
                      " to cross, type 's' for swim. If go by boat, type 'b'.\n").lower()
    if choice2 == "b":
    #game continues
        choice3 = input("You have arrived on land unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire! Game over!")
            print(""" (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure! You WIN!")
        elif choice3 == "blue":
            print("So sorry but you entered a room full of dangerous beasts that ate you alive. Game over!")
        else:
            print("You didn't choose one of the colored doors in front of you. Unfortunately crows ate your body as you waited stupidly outside of the three doors.")
    else:
        print(":( You decided to swim and you were attacked by trout. Game over!")
        print("""           ...
             .####_  .
           ;#|\_|/__/|
         ;##/ / \/ \  \
        ;##/__|O||O|__ \
       ,##|/_ \_/\_/ _\ |        OOO\
       ###| | (____) | ||       OOOOO\
       ;##\/\___/\__/\ //      OOOOOOOO
      ,;####`.      \_)/       / OOOOOOO
    ;#########`. ,,,;./       /  / DOOOOOO
  .';#################;,     /  /     DOOOO
 ,######;######;;;;####;,   /  /        DOOO
;`######`'######;;;##### ,H/  /          DOOO
#`#######`;######;;### ;##H  /            DOOO
##`#######`;######## ;####H /              DOO
`#`#######`;###### ;######H/               DOO
 ###`#######`;; ;#########HH                OO
 ####`#######`;########;###H                OO
 `#####`############;'`#;##H                O
  `#####`########;' /  / `#H
   ######`#####;'  /  /   `H """)
        
else:
    print("Oops! Sorry! You fell into a hole. Game over!")
    print('''       SSSSSS
.ss.  SP""YS
SSSS  S    S
`SS'  S.  .S
      SSSSSS
''')