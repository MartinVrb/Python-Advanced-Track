walk_minutes = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

minutes_from_walks = walk_minutes * walks_per_day
burn_calories = minutes_from_walks * 5
need_to_burn_calories = calories_per_day * 0.5

if burn_calories >= need_to_burn_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")
