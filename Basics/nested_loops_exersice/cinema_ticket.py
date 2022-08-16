command=input()
kid_tickets=0
standard_tickets=0
student_tickets=0
total_tickets=0
tickets_for_this_movie=0
while command!="Finish":
    movie_name=command
    empty_places=int(input())
    remaining_places=empty_places
    while remaining_places>0:
        type_of_ticket=input()
        if type_of_ticket=="End":
            break
        if type_of_ticket=="kid":
            kid_tickets+=1
        elif type_of_ticket=="standard":
            standard_tickets+=1
        elif type_of_ticket=="student":
            student_tickets+=1
        remaining_places-=1
        total_tickets+=1
        tickets_for_this_movie+=1

    print(f"{movie_name} - {tickets_for_this_movie/empty_places*100:.2f}% full.")
    tickets_for_this_movie=0
    command = input()
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets*100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kid_tickets/total_tickets*100:.2f}% kids tickets.")