my_list = list(map(int, input().split()))
my_number = int(input())
index = 0

while index < my_number:
    smallest_num = min(my_list)
    my_list.remove(smallest_num)
    index += 1

print(", ".join(map(str, my_list)))
