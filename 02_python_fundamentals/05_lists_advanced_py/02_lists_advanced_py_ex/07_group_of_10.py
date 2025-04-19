def group(my_numbers: list):
    for my_group in range(10, max(my_numbers) + 10, 10):
        list_with_nums = [cur_num for cur_num in my_numbers if cur_num in range(my_group - 9, my_group + 1)]
        print(f"Group of {my_group}'s: {list_with_nums}")

group(list(map(int, input().split(", "))))
