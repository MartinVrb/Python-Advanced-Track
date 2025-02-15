MAX_ENERGY = 100
ENERGY = 100
COINS = 100

working_days_list = input().split("|")
is_it = True

for command in working_days_list:
    event, num = command.split("-")
    num = int(num)

    if event == "rest":
        gained_energy = min(MAX_ENERGY - ENERGY, num)
        ENERGY += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {ENERGY}.")

    elif event == "order":
        if ENERGY >= 30:
            ENERGY -= 30
            COINS += num
            print(f"You earned {num} coins.")
        else:
            ENERGY += 50
            print("You had to rest!")

    else:
        if COINS >= num:
            COINS -= num
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            exit()

print("Day completed!")
print(f"Coins: {COINS}")
print(f"Energy: {ENERGY}")
