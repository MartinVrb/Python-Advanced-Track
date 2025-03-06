def even_numbers(numbers_list: list):
    indices = [index for index, value in enumerate(numbers_list) if value % 2 == 0]
    return indices

print(even_numbers(list(map(int, input().split(", ")))))
