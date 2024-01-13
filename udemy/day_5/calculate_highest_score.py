#you are going to write a program that calculates the highest score from a List of scores
#you are NOT allowed to use the max or min functions. the output words must match the ex:
    #'The highest score in the class is: x'

student_scores = ['76','65','89','86','55','91','64','89']
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0 #create a variable to build upon
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
#it will print in the terminal: 'The highest score in the class is: 91'
