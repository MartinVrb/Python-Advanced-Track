pair_rows = int(input())
my_dict = {}

for i in range(pair_rows):
    students_name = input()
    students_grade = float(input())

    if students_name not in my_dict:
        my_dict[students_name] = [students_grade]
    else:
        my_dict[students_name].append(students_grade)

result_dict = {}

for name, all_grades_list in my_dict.items():
    average_grade = sum(all_grades_list) / len(all_grades_list)
    if average_grade >= 4.50:
        result_dict[name] = average_grade

for key, value in result_dict.items():
    print(f"{key} -> {value:.2f}")

