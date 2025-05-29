my_words = input().split()
my_dict = {}

for element in my_words:
    element = element.lower()
    if element not in my_dict:
        my_dict[element] = 0
    my_dict[element] += 1

for key, values in my_dict.items():
    if values % 2 != 0:
        print(key, end=" ")
