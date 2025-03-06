def the_office(employees_happiness_list: list, happiness_factor: int):
    multiplied_employees_happiness = list(map(lambda x: x * happiness_factor, employees_happiness_list))
    happy_employees = list(filter(lambda x: x >= sum(multiplied_employees_happiness) / len(employees_happiness_list), multiplied_employees_happiness))
    if len(happy_employees) >= len(employees_happiness_list) // 2:
        return f"Score: {len(happy_employees)}/{len(employees_happiness_list)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(employees_happiness_list)}. Employees are not happy!"

print(the_office(list(map(int, input().split())), int(input())))
