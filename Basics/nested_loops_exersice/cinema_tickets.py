total_tickets=0
kid_tickets=0
standard_tickets=0
student_tickets=0
command=input()
while command!="Finish":
    movie_name=command
    empty_spaces = int(input())
    sold_tickets=0
    total_places=empty_spaces
    while empty_spaces>0:
        type_of_ticket=input()
        if type_of_ticket=="End":
            break
        elif type_of_ticket=="kid":
            kid_tickets+=1
        elif type_of_ticket=="standard":
            standard_tickets+=1
        elif type_of_ticket=="student":
            student_tickets+=1
        empty_spaces-=1
        sold_tickets+=1
        total_tickets+=1
    percent_full_hall=sold_tickets/total_places*100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets*100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kid_tickets/total_tickets*100:.2f}% kids tickets.")



