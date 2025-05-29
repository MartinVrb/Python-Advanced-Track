words_count = int(input())
my_dict = {}
for i in range(0, 2 * words_count, 2):
    key = input()
    value = input()
    if key not in my_dict:
        my_dict[key] = [value]
    else:
        my_dict[key].append(value)

for keys, values in my_dict.items():
    print(f"{keys} - {', '.join(values)}")
