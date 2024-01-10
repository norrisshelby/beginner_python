#conditional statements are if/else statements, ex:
#if condition: do this --> if true
#else: do this --> if condition is false

#look at the below line of code for an ex using a bathtub. The water_level
#in the tub is at 50. if it exceeds 80, we need to drain the water.
#otherwise, keep putting water into the tub. 

# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else: 
#     print("Continue.")


#COMPARISON OPERATORS PRACTICE
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to
# == is equal to --> (when you have = you are assigning a value to a variable; when you have == you are checking equality)
# != is not equal to 

#Let's come up w/ a condition to test whether someone can ride a rollercoast!
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: #a person won't be able to ride if they state they are 120 b/c > does not include 120
#how do we fix it if someone states they are 120 cm tall? we would need to code:
#if height >= 120:
   
    print("You can ride the rollercoast!")
    #else statement should NOT be put @ the same indentation as 'print'
    #the print line of code lives "inside" the if height statement 
else:
    print("Sorry, you have to grow taller before you can ride.")
#the syntax of this above code (if, else, and :) and indentation is VERY important
    