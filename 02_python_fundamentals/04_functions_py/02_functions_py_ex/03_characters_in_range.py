def character(st, en):
    for my_num in range(st + 1, en):
        new_chr = chr(my_num)
        print(new_chr, end=" ")

start = ord(input()) # 97
end = ord(input()) # 101

character(start, end)
