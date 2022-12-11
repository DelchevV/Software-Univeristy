def add_songs(*args):
    songs_dict = {}

    for info in args:
        title = info[0]
        lyrics = info[1]

        if title not in songs_dict:
            songs_dict[title] = []
        if len(lyrics) > 0:
            songs_dict[title].append(lyrics)

    result = ''
    for key, value in songs_dict.items():
        result += f'- {key}\n'
        for val in value:
            result += '\n'.join(val) + '\n'

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
