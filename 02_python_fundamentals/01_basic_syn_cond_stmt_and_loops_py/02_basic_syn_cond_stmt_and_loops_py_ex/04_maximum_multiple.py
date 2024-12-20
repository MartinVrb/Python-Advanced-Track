from sys import maxsize

divisor = int(input())
boundary = int(input())
max_num = -maxsize

for num in range(1, boundary + 1):
    if num % divisor == 0:
        if num > max_num:
            max_num = num
print(max_num)
