import math

type=input()
if type=='square':
    a=float(input())
    face=a*a;

elif type=='rectangle':
    a=float(input())
    b=float(input())
    face=a*b

elif type=='circle':
    a = float(input())
    face=math.pi*a*a

elif type=='triangle':
    a=float(input())
    b=float(input())
    face=a*b/2

print(f'{face:3f}')
