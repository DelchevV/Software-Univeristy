start_of_string = ord(input())
end_of_string = ord(input())
text = input()
result = 0
for ch in text:
    if start_of_string < ord(ch) < end_of_string:
        result += ord(ch)
print(result)

