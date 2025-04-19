def electron_distribution(electrons: int) -> list:
    my_list = []
    index = 1
    while electrons >= 0:
        result = 2 * index ** 2
        index += 1
        if electrons - result > 0:
            electrons -= result
            my_list.append(result)
        else:
            my_list.append(electrons)
            break

    return my_list

print(electron_distribution(int(input())))
