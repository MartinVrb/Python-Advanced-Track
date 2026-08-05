my_dict = {}
command = input()
while command != "end":
    course, student = command.split(" : ")
    if course not in my_dict:
        my_dict[course] = [student]
    else:
        my_dict[course].append(student)

    command = input()

for key, value in my_dict.items():
    print(f"{key}: {len(my_dict[key])}")
    for name in value:
        print(f"-- {name}")
