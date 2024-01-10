#say we wanted to sell tickets to a movie and there is a change in $ for an adult ticket
#if the moviegoer is less than or equal to 18 yoa, then they pay $7
#if the moviegoer is greater than 18, they pay $12

# <= 18 $7
# > 18  $12

#how do we represent this extra condition that we need to check for in our code?
#we could use a 'nested if/else' statement:

#NESTED IF/ELSE STATEMENTS look like:
#if condition:
    #if another condition:
        #do this
    #else:
        #do this
#else:
    #do this

#Let's practice:

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# age = int(input("What is your age? "))

# if height >= 18:
#     print("You can ride the rollercoaster!")
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.") #this is an example of a nested if/else statement b/c it lives inside an if/else statement
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# what is we had 3 possibilities?  we can use the if/elif/else 
    #otherwise known elif conditions (stands for 'else/if')
    #you can add as many elif conditions are you want
#possibilities are:
# < 12 pays $5
# 12 - 18 pays $7
# > 18 pays $12

#if condition1:
    # do A
#elif condition2:
    # do B
#else:
    # do this

print("Welcome to the rollercoast!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:   #we can use as many elif conditions we like b/w if and else statements
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")