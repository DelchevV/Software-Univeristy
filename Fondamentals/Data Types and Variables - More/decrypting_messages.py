key=int(input())
lines=int(input())
decripted_message=""
for line in range(lines):
    current_line=ord(input())
    current_letter=chr(key+current_line)
    decripted_message+=current_letter
print(decripted_message)

    