my_word = ""
n_counts = 0
c_counts = 0
o_counts = 0
command = input()

while command != "End":

    if command.isalpha() or command == "n" or command == "o" or command == "c":
        if command == "n":
            n_counts += 1
            if n_counts >= 2:
                my_word += command
        elif command == "c":
            c_counts += 1
            if c_counts >= 2:
                my_word += command
        elif command == "o":
            o_counts += 1
            if o_counts >= 2:
                my_word += command
        else:
            my_word += command

        if n_counts >= 1 and c_counts >= 1 and o_counts >= 1:
            print(my_word, end="")
            my_word = " "
            n_counts = 0
            c_counts = 0
            o_counts = 0

    command = input()

# H
# n
# e
# l
# l
# o
# o
# c
# t
# c
# h
# o
# e
# r
# e
# n
# e
# End
