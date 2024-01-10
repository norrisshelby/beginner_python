#what if we are in a situation where we need to check for multiple conditions
#even if the previous one was already true???

#if/elif/else --> only one of these things will be carried out (A, B, or C)
#multiple 'if' statements --> if all 3 conditions are checked, then A, B and C will all be executed


#in this rollercoaster ex, we want to ask the riders (of any given age) if they would like a photo of them on the ride.
#the question is, where do we put this question to ask if they would like a photo?

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