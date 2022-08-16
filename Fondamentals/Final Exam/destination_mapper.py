import re

pattern=r'([\=\/])([A-Z][A-Za-z]{2,})\1'
text=input()
matches=re.findall(pattern,text)
result=[match[1] for match in matches]

words_len=0
for res in result:
    words_len+=len(res)
print('Destinations: '+", ".join(result))
print(f'Travel Points: {words_len}')
