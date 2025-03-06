def names(names_list: list):
    result = sorted(names_list, key=lambda x: (-len(x), x))
    return result
print(names(input().split(", ")))
