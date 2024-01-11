#write a program that will select a random name from a list of names
#the person selected will have to apy for everybody's food bill
#note: you are not allowed to use the choice() function
#output should be: "<name> is going to buy the meal today!"

#names = names_string.split(", ")

#import random

# get the total number of items in the list
#num_items = len(names) --> it will tell us how many items are in the list

# generate random numbers between 0 and the last index
#random_choice = random.randint(0, num_items - 1)

#choose and print a random name
#print(names[random_choice])

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#how could we separate this into fruits and veggies?
#how could we have a list-within-a-list? we could have what's called a 'nested list'

#rewrite dirty_dozen into two separate groups to make 1 variable for each set of lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen) #there will be two brackets at the beginner and end separating both lists