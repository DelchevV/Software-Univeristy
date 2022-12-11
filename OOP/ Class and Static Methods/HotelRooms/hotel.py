from HotelRooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and \
                    (not room.is_taken) and \
                    room.capacity >= people:
                self.guests += people
                room.guests += people
                room.is_taken = True

    def free_room(self, room_number):
        for room in self.rooms:
            if room.is_taken and room.number == room_number:
                room.is_taken = False
                current_room_guests = room.guests
                room.guests=0
                self.guests -= current_room_guests

    def status(self):
        free_rooms=[str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms=[str(r.number) for r in self.rooms if r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(free_rooms)}\n" \
                 f"Taken rooms: {', '.join(taken_rooms)}"
        return result


# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())
