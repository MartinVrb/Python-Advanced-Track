start_num = int(input())
positive_list = []
negative_list = []
negative_sum = 0

for _ in range(start_num):
    cur_num = int(input())
    if cur_num >= 0:
        positive_list.append(cur_num)
    else:
        negative_sum += cur_num
        negative_list.append(cur_num)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {negative_sum}")
