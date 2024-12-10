company = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_ticket_price = float(input())
kid_ticket_price = adult_ticket_price * (1 - 0.70)

service_fee = float(input())

price_adults = adult_tickets * (adult_ticket_price + service_fee)
price_kids = kids_tickets * (kid_ticket_price + service_fee)
final_price = price_kids + price_adults
profit = final_price * 0.20

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
