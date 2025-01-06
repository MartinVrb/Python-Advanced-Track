# Solution 1:
# first_string = input()
# second_string = input()
# my_list = list(first_string)
# counter = 0
#
# for letter in second_string:
#     if my_list[counter] != letter:
#         my_list[counter] = letter
#         my_list = "".join(my_list)
#         print(my_list)
#         my_list = list(my_list)
#     counter += 1


# Solution 2:
first_string = input()
second_string = input()
last_printed_string = first_string

for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part

    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string
