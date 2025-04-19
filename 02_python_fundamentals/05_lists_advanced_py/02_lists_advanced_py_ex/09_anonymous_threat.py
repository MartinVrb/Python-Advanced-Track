def anonymous_threat(data: list):
    while True:
        command = input()

        if command == "3:1":
            return data

        command = command.split()
        action = command[0]

        if action == "merge":
            start_index = int(command[1])
            end_index = int(command[2])

            if start_index not in range(0, len(data)):
                start_index = 0

            if end_index > len(data):
                end_index = len(data) - 1

            my_new_string = "".join(data[start_index:end_index + 1])
            data[start_index:end_index + 1] = [my_new_string]

        elif action == "divide":
            index = int(command[1])
            partitions = int(command[2])

            my_string_as_list = list(data[index])
            del data[index]
            length_of_my_string = len(my_string_as_list)

            if length_of_my_string % partitions != 0:
                parts_pairs = length_of_my_string // partitions
                additional_pairs = length_of_my_string % partitions
                while len(my_string_as_list) > 0:
                    if len(my_string_as_list) == parts_pairs + additional_pairs:
                        data.insert(index, "".join(my_string_as_list[:parts_pairs + additional_pairs]))
                        del my_string_as_list[:parts_pairs + additional_pairs]
                    else:
                        data.insert(index, "".join(my_string_as_list[:parts_pairs]))
                        del my_string_as_list[:parts_pairs]
                    index += 1
            else:
                whole_parts_pairs = length_of_my_string // partitions
                while len(my_string_as_list) > 0:
                    data.insert(index, "".join(my_string_as_list[:whole_parts_pairs]))
                    del my_string_as_list[:whole_parts_pairs]
                    index += 1

print(" ".join(anonymous_threat(input().split())))