kid=0
student=0
standard=0
curent_tickets=0
cuurent_tickets_for_perc=0
total_tickets=0
movie_name=""

command=input()

while command!="Finish":
    movie_name = command
    empty_seat=int(input())
    while command!="End":
        type_of_ticket=input()
        if type_of_ticket=="kid":
            kid+=1
        elif type_of_ticket=="student":
            student+=1
        elif type_of_ticket=="standard":
            standard+=1
        total_tickets += 1
        curent_tickets+=1
        cuurent_tickets_for_perc+=1
        if curent_tickets>=empty_seat:
            curent_tickets=0
            break
        command=input()
    print(f"{movie_name} - {cuurent_tickets_for_perc/empty_seat*100}% full.")
    cuurent_tickets_for_perc=0
    command=input()
print(f"Total tickets: {total_tickets}")
print(f"{student/total_tickets*100:.2f}% student tickets.")
print(f"{standard/total_tickets*100:.2f}% standard tickets.")
print(f"{kid/total_tickets*100:.2f}% kids tickets.")

