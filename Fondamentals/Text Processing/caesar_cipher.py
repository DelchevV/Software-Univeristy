data=input()
result=""
for ch in data:
    current_ord_of_ch=ord(ch)
    new_ch=chr(current_ord_of_ch+3)
    result+=new_ch
print(result)