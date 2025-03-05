wagons = int(input())
train_list = [0] * wagons

while True:
    command = input().split()
    action = command[0]

    if action == "End":
        print(train_list)
        break

    elif action == "add":
        people = int(command[1])
        train_list[-1] += people

    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        train_list[index] += people

    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        train_list[index] -= people
