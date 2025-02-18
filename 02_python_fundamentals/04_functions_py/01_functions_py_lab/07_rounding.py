def rounded(round_the_list):
    new_list = []
    for i in round_the_list:
        new_list.append(round(i))
    return new_list

my_list = list(map(float, input().split()))
result = rounded(my_list)
print(result)

# ИЛИ
# print([round(float(my_num)) for my_num in input().split()])
