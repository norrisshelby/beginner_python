#what is randomisation? unpredicability for games/programs
#why are machines called deterministic? they will perform repeatable actions in a fully predictable way
#how do we create randomization in predictable machines running off of 1s and 0s?
    #use pseudo-random # generators, python uses the Mersenne Twister

#https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

import random # head overf to askpython.com and search for the Python random module

random_integer = random.randint(1,10) #random taps into the module above that we imporoted
print(random_integer) #this will print a random # (integer) in the terminal b/w 1 and 10, including 1 or 10

#what are modules? basically, code can get so long to the point it's hard to know what's going on in a large piece of code from top to bottom
#   people can split their code up into modules, where each module is responsible for a diff. piece of functionality of your program
#   different people can work on the different modules to create the final project

#if you create a file <file_name.py> in python, you can import that file into your code you are currently working on

#0.0000000000 - 0.999999999
random_float = random.random() #will generate a random # b/w 0 and 1 but will not include 0 or 1, will have many diff. decimal places
#how do I create a random decimal # between 0 and 5?

randomFloat = random.random() * 5 

print(randomFloat)
#remember the love_calculator_generator from day 3? instead of counting out all the letters in the person's name
# we could use a random generator (love_score = random.randint(1, 100) to print. so:

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#practice writing code below this line for a "virtual coin toss":
#if haven't already imported the random module, make sure to import it!
random_integer = random.randint(0,1)
if random_integer ==0:
    print("Tails")
else:
    print("Heads")
