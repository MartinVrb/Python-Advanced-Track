factor = int(input())
count = int(input())
my_list = []

for length in range(1, count + 1):
    my_list.append(length * factor)

print(my_list)
