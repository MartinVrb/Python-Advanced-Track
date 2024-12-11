start_num = input()
end_num = input()

s1, s2, s3, s4 = int(start_num[0]), int(start_num[1]), int(start_num[2]), int(start_num[3])
e1, e2, e3, e4 = int(end_num[0]), int(end_num[1]), int(end_num[2]), int(end_num[3])

for first_num in range(s1, e1 + 1):
    for second_num in range(s2, e2 + 1):
        for third_num in range(s3, e3 + 1):
            for fourth_num in range(s4, e4 + 1):
                if first_num % 2 != 0 and second_num % 2 != 0 and third_num % 2 != 0 and fourth_num % 2 != 0:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
