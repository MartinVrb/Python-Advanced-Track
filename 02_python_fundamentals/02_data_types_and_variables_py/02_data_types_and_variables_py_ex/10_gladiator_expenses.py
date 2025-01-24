lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

current_lost_fight = 1
helmet_expenses = 0
sword_expenses = 0
shield_expenses = 0
shield_counts = 0
armor_expenses = 0

while current_lost_fight <= lost_fights:

    if current_lost_fight % 2 == 0 and current_lost_fight % 3 == 0:
        helmet_expenses += helmet_price
        sword_expenses += sword_price
        shield_expenses += shield_price
        shield_counts += 1
        if shield_counts % 2 == 0:
            armor_expenses += armor_price
    elif current_lost_fight % 2 == 0:
        helmet_expenses += helmet_price
    elif current_lost_fight % 3 == 0:
        sword_expenses += sword_price

    current_lost_fight += 1

all_expenses = helmet_expenses + sword_expenses + shield_expenses + armor_expenses
print(f"Gladiator expenses: {all_expenses:.2f} aureus")
