
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
        c = c[:-1] #This is called slice
        res = (float(c) * 9 / 5) + 32
        return format(res , '.2f') + "F"