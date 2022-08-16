entry=input().split(" ")
result=[]
for word in entry:
    result.append(word*len(word))
print("".join(result))