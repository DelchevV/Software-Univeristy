def fill_the_box(*args):
    cube_capacity=args[0]*args[1]*args[2]
    added_cubes=0
    for elem in args[3:]:
        if added_cubes>=cube_capacity:
            cubes_left=sum(args[3:-1])-cube_capacity
            return f"No more free space! You have {cubes_left} more cubes."
        if elem=="Finish":
            cubes_left=cube_capacity-added_cubes
            return f"There is free space in the box. You could put {cubes_left} more cubes."
        else:
            added_cubes+=elem



print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))