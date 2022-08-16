import re

regex=r'\b_[A-Za-z0-9]+\b'
text=input()
matches=re.findall(regex,text)
transform="".join(matches)
regex_1=r'[^_]+'
result=re.findall(regex_1,transform)
print(",".join(result))


