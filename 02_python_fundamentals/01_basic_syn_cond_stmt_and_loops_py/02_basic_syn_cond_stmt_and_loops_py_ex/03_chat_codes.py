sent_messages = int(input())
my_message = 0

while my_message < sent_messages:
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif 86 != command < 88:
        print("GREAT!")
    else:
        print("Bye.")
    my_message += 1
