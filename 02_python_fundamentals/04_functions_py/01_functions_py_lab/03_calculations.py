def calculator(op: str, f_num: int, s_num: int):
    if op == "multiply":
        return f_num * s_num
    elif op == "divide":
        return f_num // s_num
    elif op == "add":
        return f_num + s_num
    elif op == "subtract":
        return f_num - s_num


operator = input()
first_num = int(input())
second_num = int(input())
result = calculator(operator, first_num, second_num)

print(result)
