budget = float(input())
price_per_kilo_flour = float(input())

price_per_pack_eggs = price_per_kilo_flour * 0.75
price_per_kilo_milk = price_per_kilo_flour * 1.25
price_per_250_ml = price_per_kilo_milk / 4

full_price = price_per_kilo_flour + price_per_pack_eggs + price_per_250_ml

loaves_count = 0
colored_eggs = 0

while budget >= full_price:

    budget -= full_price
    loaves_count += 1
    colored_eggs += 3

    if loaves_count % 3 == 0:
        colored_eggs -= (loaves_count - 2)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
