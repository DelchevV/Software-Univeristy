number=int(input())
is_prime=False
if number>1:
    for current_num in range(2,number):
        if number%current_num==0:
            is_prime=True
            break
if is_prime:
    print("False")
else:
    print("True")


