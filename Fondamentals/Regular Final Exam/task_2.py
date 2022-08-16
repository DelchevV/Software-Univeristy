import re

pattern=r'[!]([A-Z][a-z]{2,})[!]\:\[([A-Za-z]{8,})\]'
n_strings=int(input())
for num in range(n_strings):
    text=input()
    matches=re.findall(pattern,text)
    if matches:
        word=''
        result=[]
        for match in matches:
            word=match[1]
            command=match[0]
            result=[ord(ch) for ch in word]
            print(f"{command}: {' '.join([str(num) for num in result])}")
    else:
        print("The message is invalid")