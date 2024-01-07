import math # Use other people's code
a = float(input("Side a: ")) # the input prompts you
b = float(input("Side b: "))
# c = None # None is a placeholder in python

# Python follows PEMDAS
# print(a + b) # "+" concatenates strings but adds numbers together
# print(a*a + b*b)

'''
pythagorean theorem: a^2 + b^2 = c^2
so this means we have to do some algebra to get c by itself
so sqrt(a^2 + b^2) = sqrt(c^2)
 = sqrt(a^2 + b^2) = c
'''

c = math.sqrt(a*a + b*b)
print(c)
# print(math.sqrt(a*a + b*b))