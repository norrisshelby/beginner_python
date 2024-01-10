#This is how you work out whether if a particular year is a leap year:
#   on every yr that is divisible by 4 with NO remainder
#   EXCEPT every yr that is evenly divisible by 100 with NO remainder
#   UNLESS the yr is also divisibly by 400 with no remainder

year = int(input("Provide me with the year you would like to determine whether it is a leap year or not: "))

if year % 4 == 0:
    if year % 100 == 0: #if divisible by 100 w/ no remainders, and also by 4 w/ no remainders, it is not a leap year
    #not a leap year, unless special case
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else: 
    print("Not leap year")