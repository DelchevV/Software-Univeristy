from math import log

number = float(input())
base = input()
result = log(number) if base == "natural" else log(number, float(base))
print(f'{result:.2f}')
