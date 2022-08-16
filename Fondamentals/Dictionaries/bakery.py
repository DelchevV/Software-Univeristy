food_quantity=input().split()
bakery_dictionary={}
for index in range(0,len(food_quantity),2):
        key=food_quantity[index]
        value=food_quantity[index+1]
        bakery_dictionary[key]=int(value)
print(bakery_dictionary)
