my_num = int(input())
my_word = input()
first_list = []
filtered_list = []

for _ in range(my_num):
    additional_word = input()
    first_list.append(additional_word)
    if my_word in additional_word:
        filtered_list.append(additional_word)

print(first_list)
print(filtered_list)
