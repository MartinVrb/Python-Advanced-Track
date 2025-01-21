CAPACITY = 255
commands_count = int(input())
all_litters = 0

for _ in range(1, commands_count + 1):
    litter = int(input())
    if all_litters + litter > CAPACITY:
        print("Insufficient capacity!")
        continue
    else:
        all_litters += litter

print(all_litters)
