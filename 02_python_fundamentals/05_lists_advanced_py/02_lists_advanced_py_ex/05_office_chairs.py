def office_chairs(rooms: int):
    free_chairs = 0
    is_it_true = True

    for num_of_room in range(1, rooms + 1):
        count_chairs, visitors = input().split(" ")
        difference = len(count_chairs) - int(visitors)

        if difference < 0:
            is_it_true = False
            print(f"{abs(difference)} more chairs needed in room {num_of_room}")
        else:
            free_chairs += difference

    if is_it_true:
        print(f"Game On, {free_chairs} free chairs left")

office_chairs(int(input()))
