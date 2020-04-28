import requests
import json

weather_api_url="http://api.openweathermap.org/data/2.5/weather"
city="San%20Diego"
app_key_id="8c4bf8d800cb2d722fe41556ce81e1a7"
get_weather_info_url = weather_api_url + "?q=" + city + "&APPID=" + app_key_id
weather_bbox_url = "http://api.openweathermap.org/data/2.5/box/city"
lon_left = "12"
lat_bottom = "32"
lon_right = "15"
lat_top = "37"
zoom = "10"
get_several_cities_url = weather_bbox_url + "?bbox=12,32,15,37,10&APPID=" + app_key_id
#bbox bounding box [lon-left,lat-bottom,lon-right,lat-top,zoom]
keys = []
def main():
	res = requests.get(get_weather_info_url)
	res2 = requests.get(get_several_cities_url)
	print(get_several_cities_url)
	data = res2.json()
	get_keys(data, keys)
	print(keys)
	pretty_print(data)
	raw_cities = data['list']
	max(raw_cities)
	cities = get_cities(raw_cities)
	# To View content
	# response.text
	# response.content
	# response.json()
def pretty_print(data):
	#print(data['calctime'])
	print(json.dumps(data, indent=4, sort_keys=True))


def get_cities(raw_cities):
	cities={} # this is a dict
	for raw_city in raw_cities:
		temp = raw_city['main']['temp']
		name = raw_city['name']
		cities
		#print(raw_city['name'] + " Current Temperature = " + str(temp))
	#print(cities[0].name)


def find_hottest(cities):
	hottest=max(cities[])
	print(hottest)

def get_keys(data, keys):
	if isinstance(data, dict):
		keys += data.keys()
		map(lambda x: get_keys(x,keys), data.values())
	elif isinstance(data, list):
		map(lambda x: get_keys(x,keys), data)


class City:
	def __init__(self,name,temp):
		self.name=name
		self.temp=temp

#def find_hottest():

if __name__ == "__main__":
	main()