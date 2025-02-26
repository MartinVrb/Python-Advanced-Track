def loading_bar(major_num):
    percent_symbols = major_num // 10
    dots = 10 - percent_symbols
    my_final_string = f"[{'%' * percent_symbols}{'.' * dots}]"

    if percent_symbols < 10:
        print(f"{major_num}% {my_final_string}")
        print("Still loading...")
    else:
        print(f"{major_num}% Complete!")
        print(f"{my_final_string}")

loading_bar(int(input()))
