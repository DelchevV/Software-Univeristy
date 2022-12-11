from math import ceil


class PhotoAlbum:
    def __init__(self,pages):
        self.pages=pages
        self.photos=[[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls,photos_count):
        return cls(ceil(photos_count/4))

    def add_photo(self,label):
        for index in range(len(self.photos)):
            if len(self.photos[index])<4:
                self.photos[index].append(label)
                return f"{label} photo added successfully on " \
                       f"page {index+1} " \
                       f"slot {len(self.photos[index])}"
        return "No more free slots"

    def display(self):
        separator="-----------"
        result=[separator]
        for page in self.photos:
            result.append(("[] "*len(page)).rstrip())
            result.append(separator)
        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

