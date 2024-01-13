#for Loop with Range
#for number in range(1,10): #b/w 1-10 but NOT including 10
    #if I wanted numbers 1-10 including 10, then range(1, 11)

#you can 'step' by number in the range
# for number in range(1,11,3):
#     print(number)
#it will print: 1, 4, 7, 10

#how do we add up all the numbers in the range: (1,101) which is actually 1-100

# total = 0
# for number in range(1,101):
#     total += number
# print(total)

#it will print '5050'

target = 100
even_sum = 0
for number in range(2, target + 1, 2): #the target + 1 makes sure we go up to 100, which is the target, not 99
    even_sum += number
print(even_sum)

#or the alternative way of doing this is

# alternative_sum = 0
# for number in range(1, target + 1):
#     if number % 2 == 0:
#         alternative_sum += number
# print(alternative_sum)