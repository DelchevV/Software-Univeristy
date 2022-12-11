def forecast(*args):
    weather_locations = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for element in args:
        location, weather = element
        weather_locations[weather].append(location)

    result = ""
    for key, value in weather_locations.items():
        if len(value) > 0:
            for loc in sorted(value, key=lambda x: x):
                result += f'{loc} - {key}\n'

    return result


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
