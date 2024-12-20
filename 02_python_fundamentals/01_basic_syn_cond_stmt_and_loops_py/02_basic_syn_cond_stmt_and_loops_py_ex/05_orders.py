orders_count = int(input())
counter = 0
total_price = 0

while counter < orders_count:
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (0.01 <= price_per_capsule <= 100) and (1 <= days <= 31) and (1 <= capsules_per_day <= 2000):
        price_for_all_capsules_per_day = capsules_per_day * price_per_capsule
        price_for_all_days = price_for_all_capsules_per_day * days
        total_price += price_for_all_days
        print(f"The price for the coffee is: ${price_for_all_days:.2f}")
    counter += 1
else:
    print(f"Total: ${total_price:.2f}")
