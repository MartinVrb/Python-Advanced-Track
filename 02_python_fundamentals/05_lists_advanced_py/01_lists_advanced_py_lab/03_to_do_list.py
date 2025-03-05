# my_list = ["0"] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     order_of_importance, note = command.split("-")
#     order_of_importance = int(order_of_importance) - 1
#     my_list.pop(order_of_importance)
#     my_list.insert(order_of_importance, note)
#
# cleaned_list = [element for element in my_list if element != "0"]
# print(cleaned_list)

# Reshenie 2
def process_todo_notes():
    todo_notes = []

    while True:
        note = input()
        if note == "End":
            break
        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
    result_sorted_notes = [note.split("-")[1] for note in sorted_notes]
    return result_sorted_notes

print(process_todo_notes())
