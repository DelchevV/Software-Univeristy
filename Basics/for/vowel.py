input_text=input()
value=0
for i in input_text:
    if i=="a":
        value+=1
    elif i=="e":
        value+=2
    elif i=="i":
        value+=3
    elif i=="o":
        value+=4
    elif i=="u":
        value+=5
print(value)