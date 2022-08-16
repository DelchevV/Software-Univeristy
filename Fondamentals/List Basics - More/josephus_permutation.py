people=input().split()
execution_step=int(input())
list_of_people=[]
executed_people=[]
index_counter=0
for person in people:
    list_of_people.append(int(person))
while len(list_of_people)>0:
    for person in range(index_counter,len(list_of_people),execution_step):
        executed_people.append(person)
        index_counter+=execution_step
        if index_counter+execution_step>=len(list_of_people):
            index_counter=0
            continue
        list_of_people.remove(person)

executed_people.remove(0)
print(executed_people)