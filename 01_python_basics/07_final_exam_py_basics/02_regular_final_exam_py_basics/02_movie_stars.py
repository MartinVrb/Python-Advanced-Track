budget = float(input())

while True:
    counter = 0
    command = input()

    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    if command == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(command) <= 15:
        budget -= float(input())
    else:
        budget -= (budget * 0.20)
