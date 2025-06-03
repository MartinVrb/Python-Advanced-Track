my_dict = {}
command = input()
while command != "stop":
    if command not in my_dict:
        my_dict[command] = int(input())
    else:
        my_dict[command] += int(input())

    command = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")
