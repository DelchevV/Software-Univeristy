import sys
movies_count=int(input())
highest_rating=-sys.maxsize
name_of_highest=" "
name_of_lowest=" "
all_rating=0
lowest_rating=sys.maxsize
for movie in range(movies_count):
    movie_name=input()
    rating=float(input())
    if rating>highest_rating:
        name_of_highest=movie_name
        highest_rating=rating
    elif rating<lowest_rating:
        name_of_lowest=movie_name
        lowest_rating=rating
    all_rating+=rating
average=all_rating/movies_count
print(f"{name_of_highest} is with highest rating: {highest_rating:.1f}")
print(f"{name_of_lowest} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average:.1f}")
