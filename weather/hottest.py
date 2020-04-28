import requests
import json

locations=["SAN DIEGO", "EL PASO", "Ciudad Juarez", "Bangkok", "Kiev", "Saigon", "Auckland"]
weather_api_url = "http://api.openweathermap.org/data/2.5/weather"
app_key_id = "8c4bf8d800cb2d722fe41556ce81e1a7"
APP_ID = "APPID=" + app_key_id
weather_bbox_url = "http://api.openweathermap.org/data/2.5/box/city"
lon_left = "12"
lat_bottom = "32"
lon_right = "15"
lat_top = "37"
zoom = "10"
get_several_cities_url = weather_bbox_url + "?bbox=12,32,15,37,10" + "&" + APP_ID
# bbox bounding box [lon-left,lat-bottom,lon-right,lat-top,zoom]
cities = []


def main():
    cities_info = get_weather_info(locations)
    # [thing for thing in list_of_things] single line-loops
    [city.print_info() for city in cities]
    hottest = find_hottest(cities_info)
    print("SO HOT IN HERE! = " + hottest.name + " with a temperature of = " + str(hottest.convert_kelvin_to_fahrenheit()))

    # res2 = requests.get(get_several_cities_url)
    # print(get_several_cities_url)
    # data = res2.json()
    # get_keys(data, keys)
    # raw_cities = data['list']
    # find_hottest(raw_cities)


def get_weather_info(locations):
    for location in locations:
        get_weather_info_url = weather_api_url + "?q=" + location + "&" + APP_ID
        info = requests.get(get_weather_info_url)
        data = info.json()
        cities.append(City(data['name'],
                           data['main']['temp'],
                           data['coord']['lat'],
                           data['coord']['lon']))
    return cities


# To View content
def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def find_hottest(cities):
    hottest_city = cities[0]
    for city in cities[1:]:
        if city.temp > hottest_city.temp:
            hottest_city = city
    return hottest_city


def get_keys(data, keys):
    if isinstance(data, dict):
        keys += data.keys()
        map(lambda x: get_keys(x, keys), data.values())
    elif isinstance(data, list):
        map(lambda x: get_keys(x, keys), data)


class City:
    def __init__(self, name, temp, lat, lon):
        self.name = name
        self.temp = temp
        self.lat = lat
        self.lon = lon

    def print_info(self):
        print("Name => ", self.name, "  Temperature = ", self.temp, " In celsius = ", self.convert_kelvin_to_celsius(),
              " In Fahrenheit = ", self.convert_kelvin_to_fahrenheit())

    def convert_kelvin_to_celsius(self):
        return format(self.temp - 273.15, '.2f') + "C"

    def convert_kelvin_to_fahrenheit(self):
        # Formula is ((K - 273.15) * 9 ) / 5 + 32
        c = self.convert_kelvin_to_celsius()
        c = c[:-1]
        res = (float(c) * 9 / 5) + 32
        return format(res , '.2f') + "F"


if __name__ == "__main__":
    main()
