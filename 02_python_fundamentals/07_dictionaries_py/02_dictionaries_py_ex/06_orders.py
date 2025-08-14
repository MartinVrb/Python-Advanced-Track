dict_with_qty = {}
dict_with_prices = {}
command = input()
while command != "buy":
    name, price, qty = command.split()
    price = float(price)
    qty = int(qty)

    if name not in dict_with_qty:
        dict_with_qty[name] = qty
        dict_with_prices[name] = price
    else:
        dict_with_qty[name] += qty
        dict_with_prices[name] = price

    command = input()

final_dict = {}
for name in dict_with_qty.keys():
    final_dict[name] = dict_with_qty[name] * dict_with_prices[name]

for key, value in final_dict.items():
    print(f"{key} -> {value:.2f}")
