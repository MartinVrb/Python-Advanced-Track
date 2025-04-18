def next_version(software_version: list):
    f_num, s_num, t_num = software_version[0], software_version[1], software_version[2]
    t_num += 1
    if t_num > 9:
        t_num = 0
        s_num += 1
        if s_num > 9:
            s_num = 0
            f_num += 1

    return f"{f_num}.{s_num}.{t_num}"

print(next_version(list(map(int, input().split(".")))))
