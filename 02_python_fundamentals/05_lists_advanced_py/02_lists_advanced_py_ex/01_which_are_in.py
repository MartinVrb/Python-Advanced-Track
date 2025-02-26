def which_sequence(substrings: list, main_string: list):
    # Purvo reshenie
    new_list = []
    for my_substring in substrings:
        for my_string in main_string:
            if my_substring in my_string:
                new_list.append(my_substring)
                break
    return new_list

    # Vtoro reshenie
    # new_list = [my_substring for my_substring in substrings if any(my_substring in my_string for my_string in main_string)]
    # return new_list

print(which_sequence(input().split(", "), input().split(", ")))
