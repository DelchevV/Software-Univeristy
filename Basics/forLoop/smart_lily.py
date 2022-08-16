lili_age=int(input())
washer=float(input())
price_per_toy=float(input())
total_money=0
total_toys=0
birthday_money=0



for number in range(1,lili_age+1):
    if number%2!=0:
        total_toys += 1

    else:
        birthday_money += 10
        total_money += birthday_money - 1



total_money+= total_toys*price_per_toy
diffrence=abs(washer-total_money)
if total_money>=washer:
    print(f"Yes! {diffrence:.2f}")
else:
    print(f"No! {diffrence:.2f}")