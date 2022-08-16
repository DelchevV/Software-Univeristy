lines_of_input = (int(input()))
is_balanced = True
open_bracket = 0
closing_bracket = 0
current_bracket = ""
for line in range(lines_of_input):
    current_line = input()
    if current_bracket == "(" and "(" in current_line:
        is_balanced = False
        break
    if current_bracket == ")" and ")" in current_line:
        is_balanced = False
        break
    if "(" in current_line:
        open_bracket += 1
        current_bracket = "("
    if ")" in current_line:
        closing_bracket += 1
        current_bracket = ")"
if open_bracket==closing_bracket and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
