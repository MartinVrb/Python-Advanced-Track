def factorial_division(my_num):
    result = 1
    for fact_num in range(my_num, 0, -1):
        result *= fact_num
    return result

first_result = factorial_division(int(input()))
second_result = factorial_division(int(input()))
final_result = first_result / second_result
print(f"{final_result:.2f}")
