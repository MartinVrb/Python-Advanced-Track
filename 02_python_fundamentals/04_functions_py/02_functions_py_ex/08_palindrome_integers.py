def palindrome(f_list: list):
    true_false_list = []
    for cur_num in f_list:
        if cur_num == cur_num[::-1]:
            true_false_list.append("True")
        else:
            true_false_list.append("False")
    return true_false_list

result = palindrome(input().split(", "))
print("\n".join(result))

# def palindrome(f_list: list):
#     true_false_list = ["True" if cur_num == cur_num[::-1] else "False" for cur_num in f_list]
#     return true_false_list
#
# result = palindrome(input().split(", "))
# print("\n".join(result))
