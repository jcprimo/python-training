import requests
import json
import time
from weather.City.city import City

locations=["SAN DIEGO", "EL PASO", "Ciudad Juarez", "Bangkok", "Kiev", "Saigon", "Auckland", "Albuquerque", "Kathmandu"]
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
#####################################
# Variables set for display purposes
#####################################
tab_length = 4
total_tabs = 5
#####################################
# Prints out localtime
#####################################
# Time in seconds
# since the epoch
secs = 950000000
local_time = time.localtime()
# Determine localtime in seconds
total_seconds = ((local_time.tm_hour * 60 + local_time.tm_min) * 60) + local_time.tm_sec + local_time.tm_gmtoff

def main():
    cities_info = get_weather_info(locations)
    # This line sorts the cities by city name
    cities_info.sort(key=lambda x: x.name, reverse=False)
    # [thing for thing in list_of_things] single line-loops
    sort_by_city(cities_info)
    hottest = find_hottest(cities_info)
    print("")
    print("SO HOT IN HERE! = " + hottest.name + " with a temperature of = " + str(hottest.convert_kelvin_to_fahrenheit()))


def get_weather_info(lugares):
    for location in lugares:
        print("Location to find weather for = " + location)
        get_weather_info_url = weather_api_url + "?q=" + location + "&" + APP_ID
        info = requests.get(get_weather_info_url)
        data = info.json()
        cities.append(City(data['name'],
                           data['main']['temp'],
                           data['coord']['lat'],
                           data['coord']['lon'],
                           data['timezone']))
    return cities


# To View content
def pretty_print(data):
    print(json.dumps(data, indent=tab_length, sort_keys=True))


def find_hottest(cities):
    hottest_city = cities[0]
    for city in cities[1:]:
        if city.temp > hottest_city.temp:
            hottest_city = city
    return hottest_city


def sort_by_city(cities):
    # One line sort function method using an inline lambda function lambda x: x.date
    # The value for the key param needs to be a value that identifies the sorting property on the object
    # cities.sort(key=lambda x: x.name, reverse=False)
    print(" --------------------------------------------------------")
    print("| \t Location \t   |\t         Temperature            |")
    print(" --------------------------------------------------------")
    print("|\tCity\t\t\tCelsius \t  Farhenheit\t Kelvin |")
    print(" --------------------------------------------------------")
    x = " "
    for citi in cities:
        num_spaces = format_text(citi.name)
        temp = str(format(citi.temp, '.2f'))
        print("| " +
              str(citi.name) + num_spaces * x + citi.convert_kelvin_to_celsius() + "\t\t\t" +
              citi.convert_kelvin_to_fahrenheit() + "\t\t " + temp + " |" + " \t" + print_citi_localtime(citi) + " |")



def print_citi_localtime(citi):
    # how do you turn hours to minutes and minutes to seconds
    # 1 hour = 60 minutes
    # 1 minutes = 60 seconds soooo
    # 2 hours = 120 minutes or 2*60 = 120 and 120 minutes * 60 seconds you get 72000 seconds
    # the formula is hours * 60 = total_min * 60 = total_seconds
    citi_time = (total_seconds + abs(citi.timezone)) % (24 * 3600)
    hour = citi_time // 3600
    citi_time %= 3600
    minutes = citi_time // 60
    citi_time %= 60
    seconds = citi_time
    hour = format_time(hour)
    minutes = format_time(minutes)
    return hour + ":" + minutes


def format_time(digits):
    if digits < 10:
        return "0" + str(digits)
    return str(digits)

# return the total of tabs missing to enter
def format_text(s):
    length = len(s) + 2
    total_spaces = length - (tab_length * total_tabs)
    return abs(total_spaces)


def get_keys(data, keys):
    if isinstance(data, dict):
        keys += data.keys()
        map(lambda x: get_keys(x, keys), data.values())
    elif isinstance(data, list):
        map(lambda x: get_keys(x, keys), data)


if __name__ == "__main__":
    #print_citi_localtime()
    main()
