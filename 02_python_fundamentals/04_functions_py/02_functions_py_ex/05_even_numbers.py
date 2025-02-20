my_list = list(map(int, input().split()))
result = list(filter(lambda a: a % 2 == 0, my_list))
print(result)

# print(list(map(int, filter(lambda a: int(a) % 2 == 0, input().split()))))