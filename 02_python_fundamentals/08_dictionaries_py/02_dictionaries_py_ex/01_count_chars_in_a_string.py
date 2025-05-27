my_string = input()
my_dict = {}
for letter in my_string:
    if letter == " ":
        continue
    elif letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
