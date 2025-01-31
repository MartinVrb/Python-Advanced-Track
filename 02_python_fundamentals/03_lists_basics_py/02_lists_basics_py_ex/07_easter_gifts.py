gifts_list = input().split()

while True:
    user_input = input().split()
    command = user_input[0]
    gift = user_input[1]

    if command == "OutOfStock":
        if gift in gifts_list:
            while gift in gifts_list:
                gift_index = gifts_list.index(gift)
                gifts_list[gift_index] = "None"

    elif command == "Required":
        index = int(user_input[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif command == "JustInCase":
        gifts_list.pop()
        gifts_list.append(gift)

    else:
        break

if "None" in gifts_list:
    while "None" in gifts_list:
        gifts_list.remove("None")

print(" ".join(gifts_list))

