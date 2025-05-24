def add_lesson(lessons_schedule, lesson_title):
    if lesson_title not in lessons_schedule:
        lessons_schedule.append(lesson_title)


def insert_lesson(lessons_schedule, lesson_title, index):
    if lesson_title not in lessons_schedule:
        lessons_schedule.insert(index, lesson_title)


def remove_lesson(lessons_schedule, lesson_title):
    if lesson_title in lessons_schedule:
        lessons_schedule.remove(lesson_title)
    if f"{lesson_title}-Exercise" in lessons_schedule:
        lessons_schedule.remove(f"{lesson_title}-Exercise")


def swap_lessons(lessons_schedule, lesson1, lesson2):
    if lesson1 in lessons_schedule and lesson2 in lessons_schedule:
        idx1, idx2 = lessons_schedule.index(lesson1), lessons_schedule.index(lesson2)
        lessons_schedule[idx1], lessons_schedule[idx2] = lessons_schedule[idx2], lessons_schedule[idx1]

        if f"{lesson1}-Exercise" in lessons_schedule:
            lessons_schedule.remove(f"{lesson1}-Exercise")
            lessons_schedule.insert(idx2 + 1, f"{lesson1}-Exercise")

        if f"{lesson2}-Exercise" in lessons_schedule:
            lessons_schedule.remove(f"{lesson2}-Exercise")
            lessons_schedule.insert(idx1 + 1, f"{lesson2}-Exercise")


def add_exercise(lessons_schedule, lesson_title):
    if lesson_title in lessons_schedule:
        idx = lessons_schedule.index(lesson_title)
        if f"{lesson_title}-Exercise" not in lessons_schedule:
            lessons_schedule.insert(idx + 1, f"{lesson_title}-Exercise")
    else:
        lessons_schedule.append(lesson_title)
        lessons_schedule.append(f"{lesson_title}-Exercise")


def softuni_course(lessons_schedule: list):
    while True:
        command = input()
        if command == "course start":
            return lessons_schedule

        parts = command.split(":")
        action = parts[0]
        lesson_title = parts[1]

        if action == "Add":
            add_lesson(lessons_schedule, lesson_title)
        elif action == "Insert":
            index = int(parts[2])
            insert_lesson(lessons_schedule, lesson_title, index)
        elif action == "Remove":
            remove_lesson(lessons_schedule, lesson_title)
        elif action == "Swap":
            second_title = parts[2]
            swap_lessons(lessons_schedule, lesson_title, second_title)
        elif action == "Exercise":
            add_exercise(lessons_schedule, lesson_title)

for i, lesson in enumerate(softuni_course(input().split(", ")), start=1):
    print(f"{i}.{lesson}")
