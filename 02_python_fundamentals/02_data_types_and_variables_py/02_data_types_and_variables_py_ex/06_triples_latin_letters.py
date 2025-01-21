my_num = int(input())

for i in range(my_num):
    for j in range(my_num):
        for k in range(my_num):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
