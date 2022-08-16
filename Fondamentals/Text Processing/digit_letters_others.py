# data=input()
# nums=""
# letters=""
# others=""
# for ch in data:
#     if ch.isalpha():
#         letters+=ch
#     elif ch.isdigit():
#         nums+=str(ch)
#     else:
#         others+=str(ch)
# print(f"{nums}\n"
#       f"{letters}\n"
#       f"{others}")

# ------Решение с компрехеншън-------
# data=input()
# nums=[str(ch) for ch in data if ch.isdigit()]
# letters=[ch for ch in data if ch.isalpha()]
# others=[ch for ch in data if not ch.isdigit() and not ch.isalpha()]
# print("".join(nums))
# print("".join(letters))
# print("".join(others))

# ------Решение с функция-------
def number_filter(entry):
    nums=[str(ch) for ch in entry if ch.isdigit()]
    return "".join(nums)


def letter_filter(entry):
    letters=[ch for ch in entry if ch.isalpha()]
    return "".join(letters)


def others_filter(entry):
    others=[ch for ch in entry if not ch.isdigit() and not ch.isalpha()]
    return "".join(others)


data=input()
print(f"{number_filter(data)}\n"
      f"{letter_filter(data)}\n"
      f"{others_filter(data)}")