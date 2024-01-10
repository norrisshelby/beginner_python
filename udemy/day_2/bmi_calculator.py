#write a program that calculates the Body Mass Index (BMI) from a user's weight and height
#the BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#BMI = weight(kg)/height**2(m**2)
#note= convert the BMI to a whole # and print out a whole # in order to pass all the tests
#height input = 1.65
#weight input = 72

#PROMPT:
#make a greeting
print("Hello and welcome to the BMI calculator!")
#1st input: enter height in meters e.g.: 1.65
height = input("What is your height in meters? ")
#2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in kg? ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_result = str(bmi)
#you could also code bmi_result = int(bmi)
#print(bmi_result) to get output the BMI calculation in your terminal

print("Your BMI is " + bmi_result)


