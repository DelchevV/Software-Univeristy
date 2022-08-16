import re
result=[]
pattern = r'(www)\.([A-Za-z0-9\-]+)+(\.[A-Za-z]+)+'
line=input()
while line:
    matches=re.search(pattern,line)
    if matches:
        result.append(matches[0])
    line=input()
for res in result:
    print(res)