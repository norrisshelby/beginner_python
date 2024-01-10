#write a program that works out whether if a given 
#number is an odd or even number
#even #s can be divided by 2 w/ no remainders.
#the mdoulo is written as a percentage sign (%) in Python. 
# ^ it gives you the remainder after a division.

print("Welcome to the 'Is your number even or odd' determinator!")

number = int(input("What is your number? "))

if number % 2 == 0: #this is saying that if the number/2 has no decimal places, it is an even number
    print("Your number is even.")
else:
    print("Your number is odd.")
