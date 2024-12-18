budget = int(input())
final_price = 0

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    price = int(command)
    final_price += price
    if final_price > budget:
        print("You went in overdraft!")
        break
