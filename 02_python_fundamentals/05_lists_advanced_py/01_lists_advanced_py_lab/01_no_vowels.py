my_string_list = list(input())
vowels_list_lower = ['a', 'o', 'u', 'e', 'i']
vowels_list_upper = [word.upper() for word in vowels_list_lower]

vowels = vowels_list_lower + vowels_list_upper
filtered_list = [letter for letter in my_string_list if letter not in vowels]
new_string = "".join(filtered_list)
print(new_string)


# VTORO RESHENIE
# text = input()
# sorted_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
# print("".join(sorted_text))