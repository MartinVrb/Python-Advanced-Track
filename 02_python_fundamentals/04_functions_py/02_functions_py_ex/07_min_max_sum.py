def min_max_values(f_list: list):
    min_value = min(f_list)
    max_value = max(f_list)
    sum_values = sum(f_list)
    return (f"The minimum number is {min_value}",
            f"The maximum number is {max_value}",
            f"The sum number is: {sum_values}")

result = min_max_values(list(map(int, input().split())))
print("\n".join(result))
