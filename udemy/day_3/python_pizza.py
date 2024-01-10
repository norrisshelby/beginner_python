#small pizza (S) = $15
#medium pizza (M) = $20
#large pizza (L) = $25

#add pepperoni for small pizza (Y or N): +$2
#add pepperoni for medium/large pizza (Y or N) = +$3
#add extra cheese for any size pizza (Y or N) = +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

#for pepperoni:
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else: #otherwise, if medium or large
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
