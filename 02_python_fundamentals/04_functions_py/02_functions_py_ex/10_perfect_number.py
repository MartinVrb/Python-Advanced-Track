def perfect_number(major_num: int):
    list_with_divisors = []
    for counter in range(1, major_num):
        if major_num % counter == 0:
            list_with_divisors.append(counter)

    sum_of_divisors = sum(list_with_divisors)
    if sum_of_divisors == major_num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_number(int(input())))
