my_num = int(input())
sum_of_digits = 0
for num in range(1, my_num + 1):
    num = str(num)
    for digit in num:
        digit = int(digit)
        sum_of_digits += digit
    if sum_of_digits in (5, 7, 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
    sum_of_digits = 0
