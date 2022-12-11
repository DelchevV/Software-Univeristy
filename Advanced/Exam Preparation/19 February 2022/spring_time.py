def start_spring(**kwargs):
    names={}

    for key,value in kwargs.items():
        if value not in names:
            names[value]=[]
        names[value].append(key)

    result=sorted(names.items(),key=lambda x: (-len(x[1]),x[0]))
    final_print=''

    for res in result:
        final_print+=f"{res[0]}:"+'\n'

        for item in sorted(res[1], key=lambda x:x):
            final_print+=f"-{item}"+'\n'

    return final_print


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


