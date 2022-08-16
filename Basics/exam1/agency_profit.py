company_name=input()
adult_tickets=int(input())
kid_tickets=int(input())
price_adult_ticket=float(input())
tax=float(input())

price_kid_ticket=price_adult_ticket-price_adult_ticket*0.70
tax_adult_ticket=price_adult_ticket+tax
tax_kid_ticket=price_kid_ticket+tax
final=(tax_kid_ticket*kid_tickets+tax_adult_ticket*adult_tickets)*0.20
print(f"The profit of your agency from {company_name} tickets is {final:.2f} lv.")

