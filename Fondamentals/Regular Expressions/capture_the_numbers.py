import re

result=""
while True:
    current_text=input()
    if current_text=="":
        break
    result+=current_text+ " "

regex=r'\d+'
result=re.findall(regex,result)
print(" ".join(result))