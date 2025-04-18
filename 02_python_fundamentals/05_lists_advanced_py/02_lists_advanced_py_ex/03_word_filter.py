def word_filter(fruit_list: list):
    return [fruit for fruit in fruit_list if len(fruit) % 2 == 0]

print("\n".join(word_filter(input().split())))
