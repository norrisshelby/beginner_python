#lists --> data structure
# https://docs.python.org/3/tutorial/datastructures.html
# how do you store "grouped" pieces of data/data that is connected? ex:
# how would you store the names of the states in the US? it would be tedious if you made a variable for each state.
# how would you store data in order? like people in line - the last person shouldn't skip to the front
# lists are just a set of [ , ] with items stored inside - can be any data type, and can be mixed (strings with number with booleans)

states_of_america = ["Delaware", "South Carolina", "Mississippi"] #for ex
#what if we wanted to list the states in order of when they joined the union?
# ^^^ the order is determined by the order in the list, so "Delaware" is the first piece of data, "South Carolina" is the 2nd, etc.

#print(states_of_america[2]) --> would print out "Mississippi"
# ^^^ that is an example of using a positive index [2] but you can also use a negative index
# [-1] would start counting from the end of the list, so it would be "Mississippi" *not South Carolina b/c you can't have a -0

#so we wanted to change the name of Delaware, we could code:
states_of_america[1] = "Deltawear" #--> [ ] gets hold of the item "1" and we set it = to a new piece of data, aka Deltwear

#for the APPEND function
#states_of_america.append("Shelbyland") #append.() will append new data to the end of the list

states_of_america.extend(["Shelbyland", "Taylorland"])

print(states_of_america)

