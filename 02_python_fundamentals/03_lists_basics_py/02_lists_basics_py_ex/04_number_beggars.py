integers_string = input()
numbers_list = list(map(int, integers_string.split(", ")))
beggars_count = int(input())
beggars_list = [0] * beggars_count

for i, number in enumerate(numbers_list):
    beggars_list[i % beggars_count] += number

print(beggars_list)