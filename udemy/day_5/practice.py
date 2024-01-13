student_heights =  ['151', '145', '179']

average_height = 0

for n in range(0, len(student_heights)): #3, stops at 3
  average_height += int(student_heights[n])
average_height /= len(student_heights[n])
print(average_height)