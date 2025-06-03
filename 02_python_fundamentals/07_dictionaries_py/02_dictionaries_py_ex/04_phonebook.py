def return_dictionary(my_dict):
    command = input()
    while not command.isnumeric():
        name, phone_number = command.split("-")
        my_dict[name] = phone_number
        command = input()

    command = int(command)
    while 0 < command:
        sec_name = input()
        if sec_name in my_dict:
            print(f"{sec_name} -> {my_dict[sec_name]}")
        else:
            print(f"Contact {sec_name} does not exist.")
        command -= 1

f_dic = {}
return_dictionary(f_dic)
