new_word = ""

while True:
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue

    for letter in command:
        new_word += letter * 2

    print(new_word)
    new_word = ""
