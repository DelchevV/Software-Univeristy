c=0
o=0
n=0
command=input()
word=""
while command!="End":
    if command.isalpha()==True:
        if command=="c" and c==0:
            c+=1
            command = input()
            continue
        elif command=="c" and c>0:
            word+=command
        elif command=="o" and o==0:
            o += 1
            command = input()
            continue
        elif command=="o" and o>0:
            word+=command
        elif command=="n" and n==0:
            n+=1
            command = input()
            continue
        elif command=="n" and n>0:
            word+=command
        else:
            word+=command
        if n==1 and o==1 and c==1:
            print(word+" ")
            n=0
            o=0
            c=0
            word=""
    command = input()











a=input()
if a.isalpha()==True:
    print(a)
else:
    print("kurec")
