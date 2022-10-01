substrings = input().split()
main_color_list = ['red', 'yellow', 'blue', ]
secondary_color_list = ['orange', 'purple', 'green']

found_colors = []

while substrings:
    if len(substrings) > 1:
        first = substrings.pop(0)
        second = substrings.pop()
        substring = first + second
        substring_2 = second + first
        if substring in main_color_list or substring in secondary_color_list:
            found_colors.append(substring)
        elif substring_2 in main_color_list or substring_2 in secondary_color_list:
            found_colors.append(substring_2)
        else:
            first = first[:-1]
            second = second[:-1]
            if first:
                substrings.insert(len(substrings)//2,first)
            if second:
                substrings.insert(len(substrings)//2,second)
    else:
        substring = substrings.pop()
        if substring in main_color_list or substring in secondary_color_list:
            found_colors.append(substring)

for color in found_colors:
    if color == "orange":
        if 'red' not in found_colors or 'yellow' not in found_colors:
            found_colors.remove(color)
    elif color == "purple":
        if 'red' not in found_colors or 'blue' not in found_colors:
            found_colors.remove(color)
    elif color == 'green':
        if 'yellow' not in found_colors or 'blue' not in found_colors:
            found_colors.remove(color)
print(found_colors)
