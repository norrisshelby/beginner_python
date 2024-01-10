print("The Love Calculator is calculating your score...")


name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = name1 + name2
lower_names = combined_names.lower() #.lower() will make sure the names are lowercase, in case the user puts names in caps

t = lower_names.count("t") #the .count() function will count the number of times 't' is found in lower_names
#lower_names is the combined lower case names
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
#we can't add this together like math, so we have to turn our digits into numbers so we combine them, rather than adding them up
#str will concatenate the digits

#to check the score, we need to turn the score into integers, since we need to compare numbers against numbers
#we need to wrap the combined string into an integer to compare to other numbers

#note: in the above code ^ the score is being concatenated rather than added up as numbers.
#str(first_digit) and str(second_digit) convert the individual digits into strings, then the strings are concatenated using the + operator
#finally, the result is converted back to an integer using int()

#so, the score is not the sum of first_digit and second_digit as numeric values, instead it's a two-digit integar formed by concatenating the string representation of those digits
#if you wanted the score to be the sum of the digits, you should use the + operator directly without converting the digits to strings

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif (score >= 40) and (score <+ 50):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")

