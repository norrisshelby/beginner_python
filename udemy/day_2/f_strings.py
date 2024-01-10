#f strings make it easy to mix strings and different data types

#let's say we wanted to print:
# score = 0
# print("your score is " + score) #terminal will output an error b/c you cannot combine a string (your message in orange) and an integer (score)

# #^ this won't work. you will need to convert the score to a string to be able to use print fnc
# #so:
# print("your score is " + str(score))

#^ this is quite painful and there is a more convenient way. let's take a look at this ex:
score = 0 #int
height = 1.8 #float
isWinning = True #boolean

#instead of having to do a bunch of code and convert everything to string, try:
#f-String
print(f"your score is {score}") #terminal will output 'your score is 0'
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
# ****MAKE SURE to put the 'f' in front of the string/quotations



