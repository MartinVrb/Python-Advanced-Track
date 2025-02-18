COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

def order_function(stocks_price):
    if stocks_price  == "coffee":
        return COFFEE
    elif stocks_price == "water":
        return WATER
    elif stocks_price == "coke":
        return COKE
    elif stocks_price == "snacks":
        return SNACKS

order = lambda price, count: price * count

my_item = input()
qty = int(input())

result = order(order_function(my_item), qty)

print(f"{result:.2f}")
