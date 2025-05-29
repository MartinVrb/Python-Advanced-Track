students = {}
course_to_search = ""

while True:
    student_info = input()
    if ":" not in student_info:
        course_to_search = student_info
        break

    name, id_num, course = student_info.split(":")
    id_num = int(id_num)
    students[name] = {}
    students[name][id_num] = course

for key, values in students.items():
    for nested_keys, nested_values in values.items():
        if course_to_search.startswith(nested_values[0:3]):
            print(f"{key} - {nested_keys}")
