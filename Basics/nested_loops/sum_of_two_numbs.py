start=int(input())
end=int(input())
magic_numb=int(input())

counter=0
is_found=False

for i in range(start,end+1):
    for f in range(start,end+1):
        counter += 1
        if i+f==magic_numb:
            is_found=True
            break
    if is_found==True:
        break

if is_found:
    print(f"Combination N:{counter} ({i } + {f} = {magic_numb})")
else:
    print(f"{counter} combinations - neither equals {magic_numb}")