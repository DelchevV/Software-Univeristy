command = input()
needed_coffes=0
while command != "END":
    if command.lower() == "coding" or command.lower() == "dog" or command.lower()=="cat" or command.lower()=="movie":
        if command=="DOG" or command=="CAT" or command=="MOVIE" or command=="CODING":
            needed_coffes+=2
        else:
            needed_coffes+=1
    command = input()
if needed_coffes>5:
    print("You need extra sleep")
else:
    print(needed_coffes)


