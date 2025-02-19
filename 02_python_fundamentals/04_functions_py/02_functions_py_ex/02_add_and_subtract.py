def sum_numbers(a, b):
    my_sum = a + b
    return my_sum

def subtract(returned_result, c):
    difference = returned_result - c
    return difference

def add_and_subtract(f_num, s_num, t_num):
    result = sum_numbers(f_num, s_num)
    final_result = subtract(result, t_num)
    return final_result

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
