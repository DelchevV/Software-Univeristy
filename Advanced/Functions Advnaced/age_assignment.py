def age_assignment(*args,**kwargs):
    name_age_dict={}
    for key,value in kwargs.items():
        for name in args:
           if name[0]==key:
               name_age_dict[name]=value
    result=sorted(name_age_dict.items(),key=lambda x: x[0])
    res=''
    for r in result:
        res+=f'{r[0]} is {r[1]} years old.\n'
    return res


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))