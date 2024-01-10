3 + 5
7 - 3
3 * 2
print(6 / 3) #when we run this, it will give us a floating point number
# ^ in the terminal, it will say: 2.0
# ^ if you use the print(type(6/3)) function, it will tell you the class is a 'float'
# ^ it's just what happens with division in python, but at the end of the day, you get the result you need

print(2 ** 3) #for exponenents (2^2)
# remember, python goes the order of operations aka PEMDASLR (LR is left right)
# multiplication and division are equal in the order 
# whichever comes first (* or /) or whichever is furthest left, will be prioritzed first

print(8 / 3) #terminal would output 2.6666666665
print(int(8 / 3)) #terminal would output 2, which isn't traditionally what we do (traditionally we'd want to round)
print(round(8 / 3)) #terminal would output 3 (a whole number)
print(round(8 / 3, 2)) #this ( , ) specifies the number of digits you want to round up to
# ^ print(round(8 / 3, 2)) would round up two decimals places b/c of the 2
print(8 // 3) #this // is called 'floor division' and it's useful to use instead of int (which would just give you a whole #)

#here's something that can be a bit tricky but pay attention
result = 4 / 2 #4/2 = 2 and 2 = result
result /= 2 #since 2 = result, result(2)/ =2 = 1
print(result) #terminal will output 1

#if you wanted to calculate the score of a game, you could write:
score = 0

#the user scores a point:
#you could write score = score + 1
#you can simply use this shorthand:
score += 1

print(score) #terminal will output 1
