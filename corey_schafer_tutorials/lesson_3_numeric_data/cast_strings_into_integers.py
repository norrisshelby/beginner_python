num_1 = '100' #num_1 is set equal to a string
num_2 = '200' #num_2 is set equal to a string

num_1 = int(num_1)
num_2 = int(num_2) #this int(num_2) function casts num_2 as an integer instead of a string
#when we run this code now, it will give us 300 b/c it will have added the integers together


print(num_1 + num_2) #if we were to run this, it would print out 100200, which is incorrect b/c it concatenated it together
#to get 300, we have to "cast" these strings into integers
