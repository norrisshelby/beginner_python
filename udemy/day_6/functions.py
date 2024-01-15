#https://docs.python.org/3/library/functions.html

# print("Hello") #the name of the function followed by a set of ()
# num_char = len("Hello")
# print(num_char)

#how do we make our OWN functions?
#use 'def' --> to create or define your function
def my_function():
    print("Hello")
    print("Bye")
#if I run the code at this point, nothing will happen (*crickets* in the terminal)
#we haven't yet 'executed' the function
    
#to 'use' the function, we have to 'call' the function
my_function()
#now it will execute and will print out 'Hello' and 'Bye'