my_year = int(input())
special_year = ""

while True:
    my_year += 1
    for digit in str(my_year):
        if str(my_year).count(digit) != 1:
            special_year = ""
            break
        else:
            special_year += digit
    if special_year != "":
        print(int(special_year))
        break
