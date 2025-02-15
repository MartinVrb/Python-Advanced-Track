TRAIN_TICKET = 150
MAX_CLOTHES_PRICE = 50.00
MAX_SHOES_PRICE = 35.00
MAX_ACCESSORIES_PRICE = 20.50

things_to_buy = input().split("|")
budget = int(input())
bought_items_list = []

for item in things_to_buy:
    type_of_clothing, price = item.split("->")
    price = float(price)

    if ((type_of_clothing == "Clothes" and price <= MAX_CLOTHES_PRICE) or (type_of_clothing == "Shoes" and price <= MAX_SHOES_PRICE) or
        (type_of_clothing == "Accessories" and price <= MAX_ACCESSORIES_PRICE)):

        if budget - price >= 0:
            budget -= price
            bought_items_list.append(price)


new_prices = [round(price * 1.40, 2) for price in bought_items_list]
profit = sum(new_prices) - sum(bought_items_list)

print(" ".join(f"{price:.2f}" for price in new_prices))
print(f"Profit: {profit:.2f}")

if sum(new_prices) + budget >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
