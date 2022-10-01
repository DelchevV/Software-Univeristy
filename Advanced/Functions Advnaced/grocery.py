def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key= lambda x:(-x[1],-len(x[0]),x[0]))
    final_res=''

    for res in result:
        final_res+=f'{res[0]}: {res[1]}\n'
    return final_res

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,

))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

