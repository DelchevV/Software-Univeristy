numbers=list(map(int,input().split()))
negative_nums=[num for num in numbers if num <0]
positive=[num for num in numbers if num not in negative_nums]
print(sum(negative_nums))
print(sum(positive))
if abs(sum(negative_nums))>abs(sum(positive)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

