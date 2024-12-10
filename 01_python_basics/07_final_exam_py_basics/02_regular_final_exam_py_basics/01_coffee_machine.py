drink = input()
sugar = input()
drinks_count = int(input())

price_per_drink = 0

if drink == "Espresso":
    if sugar == "Without":
        price_per_drink = 0.90
    elif sugar == "Normal":
        price_per_drink = 1
    elif sugar == "Extra":
        price_per_drink = 1.20

elif drink == "Cappuccino":
    if sugar == "Without":
        price_per_drink = 1
    elif sugar == "Normal":
        price_per_drink = 1.20
    elif sugar == "Extra":
        price_per_drink = 1.60

elif drink == "Tea":
    if sugar == "Without":
        price_per_drink = 0.50
    elif sugar == "Normal":
        price_per_drink = 0.60
    elif sugar == "Extra":
        price_per_drink = 0.70

price_for_the_drinks = drinks_count * price_per_drink
discount = 0

if sugar == "Without":
    price_for_the_drinks *= 0.65

if drink == "Espresso" and drinks_count >= 5:
    price_for_the_drinks *= 0.75

if price_for_the_drinks > 15:
    price_for_the_drinks *= 0.80

print(f"You bought {drinks_count} cups of {drink} for {price_for_the_drinks:.2f} lv.")
