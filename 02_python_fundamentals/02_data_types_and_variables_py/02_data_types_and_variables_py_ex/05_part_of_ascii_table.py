start = int(input())
end = int(input())

for num in range(start, end + 1):
    symbol = chr(num)
    if num == end:
        print(symbol, end="")
    else:
        print(symbol, end=" ")
