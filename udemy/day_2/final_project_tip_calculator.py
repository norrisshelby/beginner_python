print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $")) #we are likely to get decimals from the user
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? ")) 

bill_with_tip = tip / 100 * bill + bill #will be a floating point # with many decimal places, we want just 2
#OR: bill_with_tip = bill * (1 + tip) / 100 --> will have a floating point number

#OR:
#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_as_amount
#total_bill = bill + total_tip_amount

bill_per_person = bill_with_tip / people  #bill_per_person will need to have only 2 decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person) #this line of code will make sure we have 2 decimal places after the decimal point!

print(f"Each person should pay: ${final_amount}")

#each person should pay: ex: $19.93 --> we will only want 2 decimal places

#here's an ex: if the bill was $150.oo, split b/w 5 people, w/ 12% tip
#each person should pay (150.00 / 5 ) * 1.12 
#how did we get 1.12?:
#12/100 = 0.12, 150 * 0.12 = 18.0, 150 + 18 = 168 or 150 * 1.12 (just add the 1 before the decimal to get ~168)
# 168/5 = 33.6
