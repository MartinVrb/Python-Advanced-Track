my_num = int(input())
counter = 0
flag = True

while counter < my_num:
    string = input()
    for symbol in string:
        if symbol in (",", ".", "_"):
            flag = False
    if flag:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
    flag = True
    counter += 1
