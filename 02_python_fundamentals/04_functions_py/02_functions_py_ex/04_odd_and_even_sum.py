def odd_and_even_sum(num_as_str: list):
    even_sum = 0
    odd_sum = 0
    for my_num in num_as_str:
        if int(my_num) % 2 == 0:
            even_sum += my_num
        else:
            odd_sum += my_num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

my_num_as_str = list(input())

print(odd_and_even_sum(my_num_as_str))
