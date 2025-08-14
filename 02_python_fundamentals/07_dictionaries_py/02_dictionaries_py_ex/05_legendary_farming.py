key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
item_obtained = False

while True:
    my_list = input().split()
    for index in range(0, len(my_list), 2):
        qty = int(my_list[index])
        material = my_list[index + 1].lower()

        if material in key_materials:
            key_materials[material] += qty
            if key_materials[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                key_materials[material] -= 250
                item_obtained = True
                break
        else:
            if material in junk_materials:
                junk_materials[material] += qty
            else:
                junk_materials[material] = qty
    if item_obtained:
        break

for key_material, value in key_materials.items():
    print(f"{key_material}: {value}")

for junk_material, qty in junk_materials.items():
    print(f"{junk_material}: {qty}")
