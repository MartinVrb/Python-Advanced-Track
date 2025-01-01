coffees_count = 0

while True:
    command = input()
    if command == "END":
        if coffees_count > 5:
            print("You need extra sleep")
        else:
            print(f"{coffees_count}")
        break

    if command.lower() in ("coding", "dog", "cat", "movie"):
        if command.islower():
            coffees_count += 1
        else:
            coffees_count += 2

