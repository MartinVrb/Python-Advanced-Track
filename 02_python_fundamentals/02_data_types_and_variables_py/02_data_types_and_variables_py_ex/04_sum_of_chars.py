count = int(input())
sum_of_values = 0

for _ in range(1, count + 1):
    symbol = input()
    ascii_value = ord(symbol)
    sum_of_values += ascii_value

print(f"The sum equals: {sum_of_values}")
