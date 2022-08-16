number=int(input())
bonus_p=0

if number<=100:
    bonus_p+=5
elif 100< number <=1000:
    bonus_p+=number*0.2
else:
    bonus_p+=number*0.1

if number%2==0:
    bonus_p+=1
elif number%10==5:
    bonus_p+=2
print(bonus_p)
print(bonus_p+number)

