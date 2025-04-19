def decipher(secret_words: list):
    new_list = []
    for my_word in secret_words:
        count_digits = sum(char.isdigit() for char in my_word)
        numbers_as_chr = chr(int(my_word[:count_digits]))
        letters_after_num = my_word[count_digits:]
        new_word = list(numbers_as_chr + letters_after_num)
        new_word[-1], new_word[1] = new_word[1], new_word[-1]
        new_list.append("".join(new_word))

    return new_list

print(" ".join(decipher(input().split())))
