my_dictionary = {}
my_final_string = "Products in stock:"
while True:
    command = input()
    if command == "statistics":
        for key, value in my_dictionary.items():
            my_final_string += f"\n- {key}: {value}"
        print(my_final_string)
        print(f"Total Products: {len(my_dictionary)}")
        print(f"Total Quantity: {sum(my_dictionary.values())}")
        break
    product, qty = command.split(": ")
    qty = int(qty)
    if product in my_dictionary.keys():
        my_dictionary[product] += int(qty)
    else:
        my_dictionary[product] = int(qty)
