lines=int(input())
reservation_guests=set()
visited_guests=set()

for line in range(lines):
    reservation_guests.add(input())

while True:
    entry=input()
    if entry=="END":
        break
    visited_guests.add(entry)
not_came_guests=reservation_guests-visited_guests
print(len(not_came_guests))
for guest in sorted(not_came_guests):
    print(guest)