First_food = input("Your first favorite food is: ")
Second_food = input("Your second favorite food is: ")
print("This is a new recipe food", First_food.capitalize(), Second_food.lower())


Bill_total = int(input("\nEnters a restaurant bill total. $"))
Fifteen_percent = 15/100 * Bill_total
Twenty_percent = 20/100 * Bill_total
print("If the tip is 15 percent, the amounts will be: $", Bill_total + Fifteen_percent)
print("If the tip is 20 percent, the amounts will be: $", Bill_total + Twenty_percent)

Base_car_price = int(input("\nHow much does a base price of a car? $"))
Tax = 25/100 * Base_car_price
License = 5/100 * Base_car_price
Dealer_prep = 52
Destination_charge = 40
print("$", Base_car_price, "+ $", Tax, "+ $", License, "+ $52 + $40 = $", Base_car_price + Tax + License + Dealer_prep + Destination_charge)
print("Actual price of the car is $", Base_car_price + Tax + License + Dealer_prep + Destination_charge)

input("\n\nPress the enter key to exit")
