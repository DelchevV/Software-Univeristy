# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

data=input()
count_chr={}
for ch in data:
    if ch==" ":
        continue
    if ch not in count_chr:
        count_chr[ch]=1
    else:
        count_chr[ch]+=1
for (key,value) in count_chr.items():
    print(key + " -> "+ str(value))