import re
number=input()
result=re.findall(r" (\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\\b",number)
print(",".join(result))