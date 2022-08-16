days=int(input())
total_food=float(input())
cat_food=0
dog_food=0
counter=0
biscuits=0
current_cat_food=0
current_dog_food=0
for day in range(days):
    counter+=1
    current_dog_food = int(input())
    current_cat_food=int(input())
    cat_food+=current_cat_food
    dog_food+=current_dog_food
    if counter%3==0:
        biscuits+=(current_cat_food+current_dog_food)*0.1
total_eaten_food=cat_food+dog_food
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food/total_food*100:.2f}% of the food has been eaten.")
print(f"{dog_food/total_eaten_food*100:.2f}% eaten from the dog.")
print(f"{cat_food/total_eaten_food*100:.2f}% eaten from the cat.")
