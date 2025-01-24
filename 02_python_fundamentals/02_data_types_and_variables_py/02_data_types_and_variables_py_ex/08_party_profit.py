group_members = int(input())
days_of_adventure = int(input())
coins = 0

for day in range(1, days_of_adventure + 1):
    coins += 50

    if day % 10 == 0:
        group_members -= 2

    if day % 15 == 0:
        group_members += 5

    coins -= (2 * group_members)

    if day % 3 == 0:
        coins -= (3 * group_members)

    if day % 5 == 0:
        coins += (20 * group_members)
        if day % 3 == 0:
            coins -= (2 * group_members)

coins_per_member = coins // group_members
print(f"{group_members} companions received {coins_per_member} coins each.")
