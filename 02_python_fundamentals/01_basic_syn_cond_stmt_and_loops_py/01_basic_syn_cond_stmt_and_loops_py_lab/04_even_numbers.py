counter = int(input())
start = 0

while start < counter:
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
    start += 1
else:
    print("All numbers are even.")
