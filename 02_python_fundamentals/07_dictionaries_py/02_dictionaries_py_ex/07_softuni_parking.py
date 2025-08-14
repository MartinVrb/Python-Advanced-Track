num_of_commands = int(input())
my_dict = {}

while num_of_commands > 0:
    command = input().split()
    username = command[1]

    if command[0] == "register":
        license_plate_num = command[2]

        if username not in my_dict:
            my_dict[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[username]}")

    elif command[0] == "unregister":
        if username not in my_dict:
            print(f"ERROR: user {username} not found")
        else:
            del my_dict[username]
            print(f"{username} unregistered successfully")

    num_of_commands -= 1

for keys, values in my_dict.items():
    print(f"{keys} => {values}")

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy