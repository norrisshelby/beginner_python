#how can we combine conditions on the same line?
#for ex:
#   if condition1 & condition2 & condition3
        #do this
#   else:
        #do this

#LOGICAL OPERATORS:
#1: AND (A and B) --> they both have to be true for the entire line to be true
        # --> if just A is true or if just B is true, then the overall code evaluates to false
#2: OR (C or D)
#3: NOT (not E) --> if the condition is false, then it becomes true, and vice versa

print("Welcome to the rollercoast!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:   #we can use as many elif conditions we like b/w if and else statements
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        #for riders between greater than and equal to 45 and less than or equal to 55, they get a free ride!
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N? ")
    if wants_photo == "Y":
        #bill = bill + 3
        #there is a simpler way of doing this, when you want to inc the current value that's held in a variable
        #and you want to save it back into the variable, write +=
        bill += 3
    #you don't have to write a commanding 'else' statement
        
    print(f"Your final bill is ${bill}.")
        # ^^^ Add $3 to the bill
        #How do we add $3 to their bill if we have only been using strings to tell them their price?
        #We will need to make a variable known as 'bill'
    
    #the question for a photo needs to be at the same indentation as this line is
else:
    print("Sorry, you have to grow taller before you can ride.")

