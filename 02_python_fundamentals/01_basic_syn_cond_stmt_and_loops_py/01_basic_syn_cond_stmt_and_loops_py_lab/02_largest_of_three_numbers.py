counter = 0
my_list = []

while counter < 3:
    number = int(input())
    my_list.append(number)
    counter += 1

print(max(my_list))
