def number_classification(numbers_list: list):
    print(f"Positive: {', '.join([p_num for p_num in numbers_list if int(p_num) >= 0])}")
    print(f"Negative: {', '.join([n_num for n_num in numbers_list if int(n_num) < 0])}")
    print(f"Even: {', '.join([e_num for e_num in numbers_list if int(e_num) % 2 == 0])}")
    print(f"Odd: {', '.join([o_num for o_num in numbers_list if int(o_num) % 2 != 0])}")

number_classification(input().split(", "))
