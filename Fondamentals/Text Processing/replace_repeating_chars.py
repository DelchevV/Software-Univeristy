data = input()
sequence = 0
result = ""

current_symbol = data[0]
result+=current_symbol
for ch in data:
    if ch != current_symbol:
        result += ch
    current_symbol = ch

print(result)
