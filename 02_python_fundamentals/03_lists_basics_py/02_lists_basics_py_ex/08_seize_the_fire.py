fire_data = input().split("#")
water_amount = int(input())

cells_list = []
total_fire = 0
total_effort = 0

for fire in fire_data:
    level_of_fire, cell_value = map(str.strip, fire.split("="))
    cell_value = int(cell_value)

    if level_of_fire == "High" and 81 <= cell_value <= 125:
        valid_fire = True
    elif level_of_fire == "Medium" and 51 <= cell_value <= 80:
        valid_fire = True
    elif level_of_fire == "Low" and 1 <= cell_value <= 50:
        valid_fire = True
    else:
        valid_fire = False


    if valid_fire and water_amount >= cell_value:
        water_amount -= cell_value
        cells_list.append(cell_value)
        total_fire += cell_value
        total_effort += cell_value * 0.25

print("Cells:")
for cell in cells_list:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
