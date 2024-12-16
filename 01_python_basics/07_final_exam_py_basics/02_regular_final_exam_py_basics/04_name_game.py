from sys import maxsize

winners_name = ""
max_num = -maxsize

while True:
    points = 0
    name = input()
    if name == "Stop":
        print(f"The winner is {winners_name} with {max_num} points!")
        break

    for letter in name:
        number = int(input())
        letters_num = ord(letter)
        if number == letters_num:
            points += 10
        else:
            points += 2

    if points >= max_num:
        max_num = points
        winners_name = name
