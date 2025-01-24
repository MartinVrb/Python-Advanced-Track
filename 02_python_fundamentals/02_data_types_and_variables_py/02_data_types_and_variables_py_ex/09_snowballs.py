snowballs_count = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for current_snowball in range(1, snowballs_count + 1):
    weight_of_snowball = int(input())
    time = int(input())
    quality = int(input())
    value = (weight_of_snowball / time) ** quality

    if value > max_value:
        max_weight = weight_of_snowball
        max_time = time
        max_quality = quality
        max_value = value

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
