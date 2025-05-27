my_list = input().split()
dictionary = {}
for i in range (0, len(my_list), 2):
    keys = my_list[i]
    values = my_list[i + 1]
    dictionary[keys] = values

products_list = input().split()
for each_product in products_list:
    if each_product in dictionary.keys():
        print(f"We have {dictionary[each_product]} of {each_product} left")
    else:
        print(f"Sorry, we don't have {each_product}")
