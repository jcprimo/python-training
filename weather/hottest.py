import requests
import json
from city import City

locations=["SAN DIEGO", "EL PASO", "Ciudad Juarez", "Bangkok", "Kiev", "Saigon", "Auckland", "Albuquerque"]
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
    # This line sorts the cities by city name
    cities_info.sort(key=lambda x: x.name, reverse=False)
    # [thing for thing in list_of_things] single line-loops
    #[city.print_info() for city in cities]
    sort_by_city(cities_info)
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

def sort_by_city(cities):
	# One line sort function method using an inline lambda function lambda x: x.date
	# The value for the key param needs to be a value that identifies the sorting property on the object
	cities.sort(key=lambda x: x.name, reverse=False)
	 
	for obj in cities:
		print("Sorted Date from obj: " +str(obj.name) + " with temperature: " + obj.convert_kelvin_to_celsius())

def get_keys(data, keys):
    if isinstance(data, dict):
        keys += data.keys()
        map(lambda x: get_keys(x, keys), data.values())
    elif isinstance(data, list):
        map(lambda x: get_keys(x, keys), data)


if __name__ == "__main__":
    main()
