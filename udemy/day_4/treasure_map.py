line1 = ["[]", "[]", "[]",]
line2 = ["[]", "[]", "[]",]
line3 = ["[]", "[]", "[]",]
map = [line1, line2, line3]
# print(map)

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? A, B, or C COMBINED with 1, 2, or 3?\n") #b3

letter = position[0].lower() #letter = b (first index of the "position" variable input)
abc = ["a", "b", "c"] #abc = strA, strB, strC

letter_index = abc.index(letter) #what is the index of the letter "b" in the variable "abc" = 1
number_index = int(position[1]) - 1 # = 2
map[number_index][letter_index] = " X " #map at 2,1

print(f"{line1}\n{line2}\n{line3}")